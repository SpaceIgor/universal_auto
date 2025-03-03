# Generated by Django 4.1 on 2023-09-13 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0048_userbank_remove_order_report_tg_driver_worked_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='fleet',
        ),
        migrations.RemoveField(
            model_name='fleets_drivers_vehicles_rate',
            name='vehicle',
        ),
        migrations.AddField(
            model_name='fleetorder',
            name='distance',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True, verbose_name='Відстань за маршрутом'),
        ),
        migrations.AlterField(
            model_name='driverefficiency',
            name='driver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.driver', verbose_name='Водій авто'),
        ),
        migrations.AlterField(
            model_name='fleets_drivers_vehicles_rate',
            name='driver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.driver', verbose_name='Водій'),
        ),
        migrations.AlterField(
            model_name='statuschange',
            name='driver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.driver'),
        ),
        migrations.AlterField(
            model_name='userbank',
            name='duty',
            field=models.IntegerField(default=0, verbose_name='Борг'),
        ),
    ]
