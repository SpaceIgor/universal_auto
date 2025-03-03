import json
import datetime
import requests
from _decimal import Decimal
from django.db.models import Q
from django.utils import timezone
from app.models import UaGpsService, Driver, Vehicle, RentInformation, Partner, FleetOrder, \
    DriverEfficiency, DriverReshuffle, CredentialPartner, ParkSettings
from auto_bot.handlers.order.utils import check_reshuffle
from auto_bot.main import bot
from scripts.redis_conn import redis_instance


class UaGpsSynchronizer:

    def __init__(self, partner_id, url=UaGpsService.get_value("BASE_URL")):
        self.url = url
        self.partner_id = partner_id
        self.session = self.get_session()

    def get_session(self):

        params = {
            'svc': 'token/login',
            'params': json.dumps({"token": CredentialPartner.get_value('UAGPS_TOKEN', partner=self.partner_id)})
        }
        login = requests.get(self.url, params=params)
        return login.json()['eid']

    def get_gps_id(self):
        if not redis_instance().exists(f"{self.partner_id}_gps_id"):
            payload = {"spec": {"itemsType": "avl_resource", "propName": "sys_name", "propValueMask": "*", "sortType": ""},
                       "force": 1, "flags": 5, "from": 0, "to": 4294967295}
            params = {
                'sid': self.session,
                'svc': 'core/search_items',
            }
            params.update({'params': json.dumps(payload)})
            response = requests.post(url=UaGpsService.get_value("BASE_URL"), params=params)
            redis_instance().set(f"{self.partner_id}_gps_id", response.json()['items'][0]['id'])
        return redis_instance().get(f"{self.partner_id}_gps_id")

    def synchronize(self):
        params = {
            'sid': self.session,
            'svc': 'core/update_data_flags',
            'params': json.dumps({"spec": [{"type": "type",
                                            "data": "avl_unit",
                                            "flags": 1,
                                            "mode": 0}]})
        }
        response = requests.get(self.url, params=params)
        for vehicle in response.json():
            Vehicle.objects.filter(licence_plate=vehicle['d']['nm'].split('(')[0]).update(gps_id=vehicle['i'])

    def generate_report(self, start_time, end_time, vehicle_id):
        road_distance = 0
        road_time = datetime.timedelta()
        parameters = {
            "reportResourceId": self.get_gps_id(),
            "reportObjectId": vehicle_id,
            "reportObjectSecId": 0,
            "reportTemplateId": 1,
            "reportTemplate": None,
            "interval": {
                "from": start_time,
                "to": end_time,
                "flags": 16777216
            }
        }

        params = {
            'svc': 'report/exec_report',
            'sid': self.session,
            'params': json.dumps(parameters)
        }
        try:
            report = requests.get(self.url, params=params)
            raw_time = report.json()['reportResult']['stats'][4][1]
            clean_time = [int(i) for i in raw_time.split(':')]
            road_time = datetime.timedelta(hours=clean_time[0], minutes=clean_time[1], seconds=clean_time[2])
            raw_distance = report.json()['reportResult']['stats'][5][1]
            road_distance = Decimal(raw_distance.split(' ')[0])
        except Exception as e:
            print(e)
        return road_distance, road_time

    @staticmethod
    def get_start_end(day=None, reshuffle=None):
        if reshuffle:
            start = timezone.localtime(reshuffle.swap_time)
            end = timezone.localtime(reshuffle.end_time)
        else:
            start = timezone.make_aware(datetime.datetime.combine(day, datetime.time.min))
            end = timezone.make_aware(datetime.datetime.combine(day, datetime.time.max))

        return start, end

    @staticmethod
    def get_timestamp(timeframe):
        return int(timeframe.timestamp())

    def get_road_distance(self, partner_id, delta=0):
        day = timezone.localtime() - datetime.timedelta(days=delta)
        road_dict = {}
        start, end = self.get_start_end(day)
        for driver in Driver.objects.filter(partner=partner_id):
            if RentInformation.objects.filter(report_from=day, driver=driver):
                continue
            road_distance = 0
            road_time = datetime.timedelta()
            completed = []
            vehicles = check_reshuffle(driver, day)
            for vehicle, reshuffles in vehicles.items():
                if reshuffles:
                    for reshuffle in reshuffles:
                        start, end = self.get_start_end(day, reshuffle)
                        completed += FleetOrder.objects.filter(driver=driver,
                                                               state=FleetOrder.COMPLETED,
                                                               accepted_time__gte=start,
                                                               accepted_time__lt=end).order_by('accepted_time')
                elif vehicle:
                    completed = FleetOrder.objects.filter(driver=driver,
                                                          state=FleetOrder.COMPLETED,
                                                          accepted_time__gte=start,
                                                          accepted_time__lt=end).order_by('accepted_time')
                else:
                    continue
                previous_finish_time = None
                for order in completed:
                    end_report = order.finish_time if order.finish_time < end else end
                    if previous_finish_time is None or order.accepted_time >= previous_finish_time:
                        report = self.generate_report(self.get_timestamp(timezone.localtime(order.accepted_time)),
                                                      self.get_timestamp(timezone.localtime(end_report)),
                                                      order.vehicle.gps_id)
                    elif order.finish_time <= previous_finish_time:
                        continue
                    else:
                        report = self.generate_report(self.get_timestamp(timezone.localtime(previous_finish_time)),
                                                      self.get_timestamp(timezone.localtime(end_report)),
                                                      order.vehicle.gps_id)
                    previous_finish_time = end_report
                    road_distance += report[0]
                    road_time += report[1]
                    order.distance = report[0]
                    order.save()
                yesterday_order = FleetOrder.objects.filter(driver=driver,
                                                            finish_time__gt=start,
                                                            accepted_time__lte=start).first()
                if yesterday_order:
                    report = self.generate_report(self.get_timestamp(start),
                                                  self.get_timestamp(timezone.localtime(yesterday_order.finish_time)),
                                                  yesterday_order.vehicle.gps_id)
                    road_distance += report[0]
                    road_time += report[1]
                if delta:
                    road_dict[driver] = (road_distance, road_time)
                else:
                    road_dict[driver] = (road_distance, road_time, previous_finish_time)
        return road_dict

    def total_per_day(self, gps_id, day=None, reshuffle=None):
        start, end = self.get_start_end(day, reshuffle)

        distance = self.generate_report(self.get_timestamp(start),
                                        self.get_timestamp(end),
                                        gps_id)[0]
        return distance

    def calc_total_km(self, driver, day):
        total_km = 0
        vehicles = check_reshuffle(driver, day)
        for vehicle, reshuffles in vehicles.items():
            if reshuffles:
                for reshuffle in reshuffles:
                    total_km += self.total_per_day(reshuffle.swap_vehicle.gps_id,
                                                   day, reshuffle)
            elif vehicle:
                total_km = self.total_per_day(driver.vehicle.gps_id, day)
        return total_km

    def save_daily_rent(self, delta):
        day = timezone.localtime() - datetime.timedelta(days=delta)
        in_road = self.get_road_distance(self.partner_id, delta=delta)
        for driver, result in in_road.items():
            distance, road_time = result
            total_km = self.calc_total_km(driver, day)

            rent_distance = total_km - distance
            DriverEfficiency.objects.filter(driver=driver, report_from=day).update(road_time=road_time)
            RentInformation.objects.create(report_from=day,
                                           driver=driver,
                                           partner=Partner.get_partner(self.partner_id),
                                           rent_distance=rent_distance)

    def check_today_rent(self):
        start = timezone.make_aware(datetime.datetime.combine(timezone.localtime(), datetime.time.min))
        in_road = self.get_road_distance(self.partner_id)
        for driver, result in in_road.items():
            distance, road_time, end_time = result
            total_km = 0
            if not end_time:
                end_time = timezone.localtime()
            vehicles = check_reshuffle(driver)
            for vehicle, reshuffles in vehicles.items():
                if reshuffles:
                    for reshuffle in reshuffles:
                        if reshuffle.end_time < end_time:
                            total_km += self.total_per_day(reshuffle.swap_vehicle.gps_id,
                                                           reshuffle=reshuffle)
                        elif reshuffle.swap_time < end_time:
                            total_km += self.generate_report(self.get_timestamp(reshuffle.swap_time),
                                                             self.get_timestamp(end_time),
                                                             reshuffle.swap_vehicle.gps_id)[0]
                        else:
                            continue
                elif vehicle:
                    total_km = self.generate_report(self.get_timestamp(start),
                                                    self.get_timestamp(end_time),
                                                    driver.vehicle.gps_id)[0]
            rent_distance = total_km - distance
            time = timezone.localtime(end_time).strftime("%H:%M")
            bot.send_message(chat_id=ParkSettings.get_value("DEVELOPER_CHAT_ID"),
                             text=f"Орендовано на {time} {driver} - {rent_distance}")
