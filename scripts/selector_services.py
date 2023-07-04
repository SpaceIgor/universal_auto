# States [key its NameService+Func in class]

bolt_states = {
    'REQUEST_BOLT_LOGIN_URL': ('https://fleetownerportal.live.boltsvc.net/fleetOwnerPortal/', 'url'),
    'R_BOLT_ADD_DRIVER_1': ("https://node.taxify.eu/fleet-registration/driverPortal/", 'url'),
    'BASE_URL': ('https://fleets.bolt.eu', 'url'),
    'BOLT_LOGIN_URL': ('https://fleets.bolt.eu/v2/login', 'url'),
    'BOLT_DOWNLOAD_PAYMENTS_ORDER_URL': ('https://fleets.bolt.eu/v2/58225/reports', 'url'),
    'BOLT_DRIVERS_URL': ('https://fleets.bolt.eu/v2/58225/drivers', 'url'),
    'BOLT_MAP_URL': ('https://fleets.bolt.eu/v2/58225/liveMap', 'url'),
    'BOLT_LOGIN_1': ('email', 'ID'),
    'BOLT_LOGIN_2': ('current-password', 'ID'),
    'BOLT_LOGIN_3': ('//button[@type="submit"]', 'XPATH'),
    'BOLT_DOWNLOAD_PAYMENTS_ORDER_1': ('//div[contains(@class, "max-w-[240px]")]//button', 'xpath'),
    'BOLT_DOWNLOAD_PAYMENTS_ORDER_2': ('//div[contains(@class, "react-datepicker-wrapper")]//input', 'XPATH'),
    'BOLT_DOWNLOAD_PAYMENTS_ORDER_3': ('//div[@tabindex="0" and @role="option"]/preceding::div', 'XPATH'),
    'BOLT_DOWNLOAD_PAYMENTS_ORDER_4': ('//div[@tabindex="0" and @role="option"]', 'XPATH'),
    'BOLT_DOWNLOAD_PAYMENTS_ORDER_5': ('//li[@role="menuitem"][3]', 'XPATH'),
    'BOLT_DOWNLOAD_PAYMENTS_ORDER_6': ('//div[contains(@class, "justify-end")]/button', 'XPATH'),
    'BOLT_DOWNLOAD_PAYMENTS_ORDER_7': ('//button[@aria-label="Previous month"]', 'XPATH'),
    'BOLT_ADD_DRIVER_1': ('//div[@role="tablist"]/preceding-sibling::div//button', 'XPATH'),
    'BOLT_ADD_DRIVER_2': ('email', 'ID'),
    'BOLT_ADD_DRIVER_3': ('phone', 'ID'),
    'BOLT_ADD_DRIVER_4': ('//div[@class="add-new-driver-dialog"]/following-sibling::footer//button', 'XPATH'),
    'BOLT_ADD_DRIVER_5': ('//a[@rel="noopener"]', 'XPATH'),
    'BOLT_ADD_DRIVER_6': ('//input[@id="first_name"]', 'XPATH'),
    'BOLT_ADD_DRIVER_7': ('//input[@id="last_name"]', 'XPATH'),
    'BOLT_ADD_DRIVER_8': ('//button[@type="submit"]', 'XPATH'),
    'BOLT_ADD_DRIVER_9': ('//div[@class="form-group"]', 'XPATH'),
    'BOLT_ADD_DRIVER_10': ("//div[contains(@class, 'show')]//span[text()=", 'XPATH'),
    'BOLT_ADD_DRIVER_11': ('//label[contains(@class, "file-upload")]', 'XPATH'),
    'BOLT_ADD_DRIVER_12': ("./input", 'XPATH'),
    'BOLT_ADD_DRIVER_13': ("//button[@type='submit']", 'XPATH'),
    'BOLT_GET_DRIVERS_TABLE_1': ('//table[@role="grid"]', 'XPATH'),
    'BOLT_GET_DRIVERS_TABLE_2': ('//table[@role="grid"]//tr[@tabindex="-1"]', 'XPATH'),
    'BOLT_GET_DRIVERS_TABLE_3': ('.//button', 'XPATH'),
    'BOLT_GET_DRIVERS_TABLE_4': ('//div[contains (@class, "leading-6")]//div[4]//p', 'XPATH'),
    'BOLT_GET_DRIVERS_TABLE_5': ('//div[contains (@class, "leading-6")]//div[5]//p', 'XPATH'),
    'BOLT_GET_DRIVERS_TABLE_6': ('//span[contains (@class, "truncate")]', 'XPATH'),
    'BOLT_GET_DRIVER_STATUS_1': ('//div[contains(@class, "map-overlay")]', 'XPATH'),
    'BOLT_GET_DRIVER_STATUS_FROM_MAP_1': ("//button[@aria-label='Close']", 'XPATH'),
    'BOLT_GET_DRIVER_STATUS_FROM_MAP_2': ('//div[@role="tab"]', 'XPATH'),
    'BOLT_GET_DRIVER_STATUS_FROM_MAP_3': (
        '//div[contains(@class, "map-overlay")]/div/div/div[@role="button"][', 'XPATH'),
    'BOLT_GET_DRIVER_STATUS_FROM_MAP_3.1': (']/div/div/div[1]/span/span', 'XPATH'),
    'BOLT_DISABLE_CASH_1': ('//tr[@role="row"]//p[contains(text(), "', 'XPATH'),
    'BOLT_DISABLE_CASH_2': ('//div[@class="my-auto"]', 'XPATH'),
    'BOLT_DISABLE_CASH_3': ('//div[contains(@class, "max-w-md")]//button[contains(@class, "text-key-light")]', 'XPATH'),

}

newuklon_states = {
    'BASE_URL': ('https://fleets.uklon.com.ua', 'url'),
    'NEWUKLON_LOGIN_1': ('https://fleets.uklon.com.ua/auth/login', 'url'),
    'NEWUKLON_LOGIN_2': ('//input[@data-cy="phone-number-control"]', 'XPATH'),
    'NEWUKLON_LOGIN_3': ('//input[@data-cy="password"]', 'XPATH'),
    'NEWUKLON_LOGIN_4': ('//button[@data-cy="login-btn"]', 'XPATH'),
    'NEWUKLON_DOWNLOAD_PAYMENTS_ORDER_1': ('https://fleets.uklon.com.ua/workspace/orders', 'url'),
    'NEWUKLON_DOWNLOAD_PAYMENTS_ORDER_2': ('//flt-group-filter[1]/flt-date-range-filter/mat-form-field/div', 'xpath'),
    'NEWUKLON_DOWNLOAD_PAYMENTS_ORDER_3': ('//mat-option/span/div[text()=" Вибрати період "]', 'XPATH'),
    'NEWUKLON_DOWNLOAD_PAYMENTS_ORDER_4': ('//input', 'XPATH'),
    'NEWUKLON_DOWNLOAD_PAYMENTS_ORDER_5': ('//span[text()= " Застосувати "]', 'XPATH'),
    'NEWUKLON_DOWNLOAD_PAYMENTS_ORDER_6': ('//span[text()=" Минулий тиждень "]', 'XPATH'),
    'NEWUKLON_DOWNLOAD_PAYMENTS_ORDER_7': ('//flt-filter-group/div/div/button', 'XPATH'),
    'NEWUKLON_ADD_DRIVER_1': ('https://partner-registration.uklon.com.ua/registration', 'url'),
    'NEWUKLON_ADD_DRIVER_2': ("//span[text()='Обрати зі списку']", 'XPATH'),
    'NEWUKLON_ADD_DRIVER_3': ("//div[@class='region-name' and contains(text(),'Київ')]", 'XPATH'),
    'NEWUKLON_ADD_DRIVER_4': ("//button[@color='accent']", 'XPATH'),
    'NEWUKLON_ADD_DRIVER_5': ("//input[@type='tel']", 'XPATH'),
    'NEWUKLON_ADD_DRIVER_6': ("//input", 'XPATH'),
    'NEWUKLON_ADD_DRIVER_7': ("//label[@for='registration-type-fleet']", 'XPATH'),
    'NEWUKLON_ADD_DRIVER_8': ("//input[@type='file']", 'XPATH'),
    'NEWUKLON_ADD_DRIVER_9': ("//button[contains(@class, 'green')]", 'XPATH'),
    'NEWUKLON_ADD_DRIVER_10': ("mat-input-2", 'XPATH'),
    'NEWUKLONS_GET_DRIVERS_TABLE_1': ('https://fleets.uklon.com.ua/workspace/drivers', 'url'),
    'NEWUKLONS_GET_DRIVERS_TABLE_2': ('//upf-drivers-list[@data-cy="driver-list"]', 'XPATH'),
    'NEWUKLONS_GET_DRIVERS_TABLE_3.1': ('//cdk-row[', 'XPATH'),
    'NEWUKLONS_GET_DRIVERS_TABLE_3.2': (']/cdk-cell[@data-cy="cell-FullName"]//a', 'XPATH'),
    'NEWUKLONS_GET_DRIVERS_TABLE_4': ('//span[@data-cy="driver-name"]', 'XPATH'),
    'NEWUKLONS_GET_DRIVERS_TABLE_5': ('//dd[@data-cy="driver-email"]', 'XPATH'),
    'NEWUKLONS_GET_DRIVERS_TABLE_6': ('//span[@data-cy="driver-phone"]', 'XPATH'),
    'NEWUKLONS_GET_DRIVERS_TABLE_7': ('//dd[@data-cy="driver-signal"]', 'XPATH'),
    'NEWUKLONS_GET_DRIVERS_TABLE_8': ('//div[@class="mat-tab-labels"]/div[@aria-posinset="5"]', 'XPATH'),
    'NEWUKLONS_GET_DRIVERS_TABLE_9': ('//div[contains(@class, "restriction-group__item")][3]//input', 'XPATH'),
    'NEWUKLONS_GET_DRIVERS_TABLE_10': ('//div/a[contains(@class, "tw-font-medium")]', 'XPATH'),
    'NEWUKLONS_GET_DRIVERS_TABLE_11': ('//span[@data-cy="license-plate"]', 'XPATH'),
    'NEWUKLONS_GET_DRIVERS_TABLE_12': ('//span[@data-cy="make-model-year"]', 'XPATH'),
    'NEWUKLONS_GET_DRIVERS_TABLE_13': ('//dd[@data-cy="vin-code"]', 'XPATH'),
    'NEWUKLONS_GET_DRIVER_STATUS_FROM_MAP_1': ("//div[contains(@class, 'panel-item')]", 'XPATH'),
    'NEWUKLONS_GET_DRIVER_STATUS_FROM_MAP_2.0': ('.//div[@class="info"]/span', 'XPATH'),
    'NEWUKLONS_GET_DRIVER_STATUS_FROM_MAP_2.1': ('//upf-map-driver-details[', 'XPATH'),
    'NEWUKLONS_GET_DRIVER_STATUS_FROM_MAP_2.2': ("]//div[contains(@class, 'tw-text-base')]", 'XPATH'),
    'NEWUKLONS_GET_DRIVER_STATUS_FROM_MAP_3': ("//button[contains(@class, 'back-btn')]", 'XPATH'),
    'NEWUKLONS_GET_DRIVER_STATUS_1': ('https://fleets.uklon.com.ua/workspace/live-map', 'url'),
    'NEWUKLONS_GET_DRIVER_STATUS_2': ('//div[contains(@class, "map-header")]', 'xpath'),
    'NEWUKLONS_WITHDRAW_MONEY_1': ('https://fleets.uklon.com.ua/workspace/finance', 'url'),
    'NEWUKLONS_WITHDRAW_MONEY_2': ('//div[@class="mat-tab-labels"]/div[2]', 'xpath'),
    'NEWUKLONS_WITHDRAW_MONEY_3': ('//span[@class="mat-checkbox-inner-container"]', 'XPATH'),
    'NEWUKLONS_WITHDRAW_MONEY_4': ('//input[@formcontrolname="remaining"]', 'XPATH'),
    'NEWUKLONS_WITHDRAW_MONEY_5': ('//div[contains (@class, "tw-col-span-5")]/button[1]', 'XPATH'),
    'NEWUKLONS_WITHDRAW_MONEY_6': ('//button[@data-cy="transfer-btn"]', 'XPATH'),
    'NEWUKLONS_DETACHING_THE_DRIVER_FROM_THE_CAR_1': ('https://fleets.uklon.com.ua/workspace/vehicles', 'XPATH'),
    'NEWUKLONS_DETACHING_THE_DRIVER_FROM_THE_CAR_2': ('//input', 'XPATH'),
    'NEWUKLONS_DETACHING_THE_DRIVER_FROM_THE_CAR_3': ('//div/div[2]/button/span[1]', 'XPATH'),
    'NEWUKLONS_DETACHING_THE_DRIVER_FROM_THE_CAR_4': ('//div/div[4]/button[2]/span[1]', 'XPATH'),
    'NEWUKLONS_DISABLE_CASH_1': ('//a[@data-cy="link" and contains(text(), "', 'XPATH'),
    'NEWUKLONS_DISABLE_CASH_2': ('//div[contains(@class, "restriction-group__item")][3]//label/span', 'XPATH'),
    'NEWUKLONS_DISABLE_CASH_3': ('//button[@type="button"]/span[@class="mat-button-wrapper"]', 'XPATH')
}

uagps_states = {
    'BASE_URL': ('https://uagps.net/wialon/ajax.html', 'url'),
}

uber_states = {
    'BASE_URL': ('https://supplier.uber.com', 'url'),
    'UBER_LOGIN_V2_1': ('https://drivers.uber.com/', 'url'),
    'UBER_LOGIN_V2_2.1': ('PHONE_NUMBER_or_EMAIL_ADDRESS', 'ID'),
    'UBER_LOGIN_V2_2.2': ('forward-button', 'ID'),
    'UBER_LOGIN_V2_3.1': ('PASSWORD', 'ID'),
    'UBER_LOGIN_V2_3.2': ('forward-button', 'ID'),
    'UBER_LOGIN_V3_1': ('https://auth.uber.com/v2/', 'url'),
    'UBER_LOGIN_V3_2.1': ('PHONE_NUMBER_or_EMAIL_ADDRESS', 'ID'),
    'UBER_LOGIN_V3_2.2': ('forward-button', 'ID'),
    'UBER_LOGIN_V3_3': ('alt-PASSWORD', 'ID'),
    'UBER_PASSWORD_FORM_V3_1': ('PASSWORD', 'ID'),
    'UBER_PASSWORD_FORM_V3_2': ('forward-button', 'ID'),
    'UBER_LOGIN_1': ('https://auth.uber.com/login/', 'url'),
    'UBER_LOGIN_2.1': ('userInput', 'CLASS_NAME'),
    'UBER_LOGIN_2.2': ('next-button-wrapper', 'CLASS_NAME'),
    'UBER_LOGIN_3.1': ('password', 'CLASS_NAME'),
    'UBER_LOGIN_3.2': ('next-button-wrapper', 'CLASS_NAME'),
    'UBER_GENERATE_PAYMENTS_ORDER_1': (
        'https://supplier.uber.com/orgs/49dffc54-e8d9-47bd-a1e5-52ce16241cb6/reports', 'url'),
    'UBER_GENERATE_PAYMENTS_ORDER_2': ('//div[@data-testid="report-type-dropdown"]/div/div', 'xpath'),
    'UBER_GENERATE_PAYMENTS_ORDER_3': ('//ul/li/div[text()[contains(.,"Payments Driver")]]', 'XPATH'),
    'UBER_GENERATE_PAYMENTS_ORDER_4': ('//ul/li/div[text()[contains(.,"Платежи (водитель)")]]', 'XPATH'),
    'UBER_GENERATE_PAYMENTS_ORDER_5': ('//button[@data-tracking-name="custom-date-range"]', 'XPATH'),
    'UBER_GENERATE_PAYMENTS_ORDER_6': ('//div[@data-baseweb="base-input"][1]', 'XPATH'),
    'UBER_GENERATE_PAYMENTS_ORDER_7': ('//button[@aria-label="Next month."]', 'XPATH'),
    'UBER_GENERATE_PAYMENTS_ORDER_8': ('//button[@aria-label="Previous month."]', 'XPATH'),
    'UBER_GENERATE_PAYMENTS_ORDER_9': ('//div[@aria-roledescription="button"]/div[text()=', 'XPATH'),
    'UBER_GENERATE_PAYMENTS_ORDER_10': ('//div[@data-baseweb="base-input"][2]', 'XPATH'),
    'UBER_GENERATE_PAYMENTS_ORDER_11': ('//button[@aria-live="polite"][1]', 'XPATH'),
    'UBER_GENERATE_PAYMENTS_ORDER_12': ('//li[@role="option" and text()[contains(.,"', 'XPATH'),
    'UBER_GENERATE_PAYMENTS_ORDER_13': ('//button[@aria-live="polite"][2]', 'XPATH'),
    'UBER_GENERATE_PAYMENTS_ORDER_14': ('//button[@data-testid="generate-report-button"]', 'XPATH'),
    'UBER_GENERATE_TRIPS_1': ('//ul/li/div[text()[contains(.,"Trip Activity")]]', 'XPATH'),
    'UBER_GENERATE_TRIPS_2': ('//ul/li/div[text()[contains(.,"Информация о поездке")]]', 'XPATH'),
    'UBER_DOWNLOAD_PAYMENTS_ORDER_1': ('(//div[@data-testid="paginated-table"]//button)[1]', 'XPATH'),
    'UBER_DOWNLOAD_PAYMENTS_ORDER_2': ('//i[@class="_css-bvkFtm"]', 'XPATH'),
    'UBER_OTP_CODE_V2_1': ('PHONE_SMS_OTP-0', 'ID'),
    'UBER_OTP_CODE_V2_2': ('PHONE_SMS_OTP-1', 'ID'),
    'UBER_OTP_CODE_V2_3': ('PHONE_SMS_OTP-2', 'ID'),
    'UBER_OTP_CODE_V2_4': ('PHONE_SMS_OTP-3', 'ID'),
    'UBER_OTP_CODE_V2_5': ('forward-button', 'ID'),
    'UBER_OTP_CODE_V1_1': ('verificationCode', 'ID'),
    'UBER_OTP_CODE_V1_2': ("next-button-wrapper", 'CLASS_NAME'),
    'UBER_FORCE_OPT_FORM': ('alt-PHONE-OTP', 'ID'),
    'UBER_ADD_DRIVER_1': ('https://supplier.uber.com/orgs/49dffc54-e8d9-47bd-a1e5-52ce16241cb6/drivers', 'url'),
    'UBER_ADD_DRIVER_2': ('//button', 'XPATH'),
    'UBER_ADD_DRIVER_3': ('//div[2]/div/input', 'XPATH'),
    'UBER_ADD_DRIVER_4': ('//div[5]/div[2]/button', 'XPATH'),
    'UBERS_GET_ALL_VEHICLES_1': ('https://supplier.uber.com/orgs/49dffc54-e8d9-47bd-a1e5-52ce16241cb6/vehicles', 'url'),
    'UBERS_GET_ALL_VEHICLES_2': ('//div[@data-testid="paginated-table"]', 'xpath'),
    'UBERS_GET_ALL_VEHICLES_3': ('//div[@data-tracking-name="vehicle-table-row"]', 'xpath'),
    'UBERS_GET_ALL_VEHICLES_4': ('div/div/div[@data-testid="vehicle-info"]', 'xpath'),
    'UBERS_GET_ALL_VEHICLES_5': ('div[3]/div/div[1]', 'xpath'),
    'UBERS_GET_ALL_VEHICLES_6': ('div[3]/div/div[2]', 'xpath'),
    'UBERS_GET_DRIVERS_TABLE_1': ('https://supplier.uber.com/orgs/49dffc54-e8d9-47bd-a1e5-52ce16241cb6/drivers', 'url'),
    'UBERS_GET_DRIVERS_TABLE_2': ('//div[@data-tracking-name="drivers"]', 'XPATH'),
    'UBERS_GET_DRIVERS_TABLE_3': ('//div[@data-tracking-name="driver-table-row"]', 'XPATH'),
    'UBERS_GET_DRIVERS_TABLE_4': ('div[1]/div[2]/div[1]', 'XPATH'),
    'UBERS_GET_DRIVERS_TABLE_5': ('div[4]/div/div[2]', 'XPATH'),
    'UBERS_GET_DRIVERS_TABLE_6': ('div[4]/div/div[1]', 'XPATH'),
    'UBERS_GET_DRIVERS_TABLE_7': ('//div[@data-tracking-name="search"]', 'XPATH'),
    'UBERS_GET_DRIVERS_TABLE_8': ('div[3]/span/div/div/div/div', 'XPATH'),
    'UBERS_GET_DRIVERS_TABLE_9': ('//div[@data-baseweb="popover"]//div[@data-testid="vehicle-search-row"][1]', 'XPATH'),
    'UBERS_GET_DRIVER_STATUS_1': (
        'https://supplier.uber.com/orgs/49dffc54-e8d9-47bd-a1e5-52ce16241cb6/livemap', 'XPATH'),
    'UBERS_GET_DRIVER_STATUS_2': ('//div[@data-tracking-name="livemap"]', 'XPATH'),
}

states = {
    'UKLON_SESSION': ('https://fleets.uklon.com.ua/api/auth', 'url'),
    'UKLON_1': ('https://fleets.uklon.com.ua/api/fleets/', 'url'),
    'UKLON_2': ('/vehicles"]', 'url'),
    'UKLON_3': ('https://fleets.uklon.com.ua/api/fleets/reports/', 'url'),
    'UKLON_4': ('/orders', 'url'),
    'UKLON_5': ('https://fleets.uklon.com.ua/api/geolocation/', 'url'),
    'UKLON_6': ('/drivers', 'url'),
}