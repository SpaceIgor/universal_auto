# Generated by Django 4.1 on 2023-05-30 14:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0026_order_checked_alter_order_car_delivery_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='role',
        ),
        migrations.AlterField(
            model_name='client',
            name='role',
            field=models.CharField(choices=[('CLIENT', 'Client'), ('DRIVER', 'Driver'), ('DRIVER_MANAGER', 'Driver manager'), ('SERVICE_STATION_MANAGER', 'Service station manager'), ('SUPPORT_MANAGER', 'Support manager'), ('OWNER', 'Owner')], default='CLIENT', max_length=50),
        ),
        migrations.AlterField(
            model_name='drivermanager',
            name='role',
            field=models.CharField(choices=[('CLIENT', 'Client'), ('DRIVER', 'Driver'), ('DRIVER_MANAGER', 'Driver manager'), ('SERVICE_STATION_MANAGER', 'Service station manager'), ('SUPPORT_MANAGER', 'Support manager'), ('OWNER', 'Owner')], default='DRIVER_MANAGER', max_length=50),
        ),
        migrations.AlterField(
            model_name='owner',
            name='role',
            field=models.CharField(choices=[('CLIENT', 'Client'), ('DRIVER', 'Driver'), ('DRIVER_MANAGER', 'Driver manager'), ('SERVICE_STATION_MANAGER', 'Service station manager'), ('SUPPORT_MANAGER', 'Support manager'), ('OWNER', 'Owner')], default='OWNER', max_length=50),
        ),
        migrations.AlterField(
            model_name='servicestationmanager',
            name='role',
            field=models.CharField(choices=[('CLIENT', 'Client'), ('DRIVER', 'Driver'), ('DRIVER_MANAGER', 'Driver manager'), ('SERVICE_STATION_MANAGER', 'Service station manager'), ('SUPPORT_MANAGER', 'Support manager'), ('OWNER', 'Owner')], default='SERVICE_STATION_MANAGER', max_length=50),
        ),
        migrations.AlterField(
            model_name='supportmanager',
            name='role',
            field=models.CharField(choices=[('CLIENT', 'Client'), ('DRIVER', 'Driver'), ('DRIVER_MANAGER', 'Driver manager'), ('SERVICE_STATION_MANAGER', 'Service station manager'), ('SUPPORT_MANAGER', 'Support manager'), ('OWNER', 'Owner')], default='SUPPORT_MANAGER', max_length=50),
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Park',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Імя автопарка')),
                ('partner', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.partner')),
            ],
            options={
                'verbose_name': 'Автопарк',
                'verbose_name_plural': 'Автопарки',
            },
        ),
        migrations.AddField(
            model_name='boltpaymentsorder',
            name='partner',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.partner'),
        ),
        migrations.AddField(
            model_name='driver',
            name='partner',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.partner'),
        ),
        migrations.AddField(
            model_name='drivermanager',
            name='partner',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.partner'),
        ),
        migrations.AddField(
            model_name='fleets_drivers_vehicles_rate',
            name='partner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.partner'),
        ),
        migrations.AddField(
            model_name='newuklonpaymentsorder',
            name='partner',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.partner'),
        ),
        migrations.AddField(
            model_name='ninjapaymentsorder',
            name='partner',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.partner'),
        ),
        migrations.AddField(
            model_name='order',
            name='partner',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.partner'),
        ),
        migrations.AddField(
            model_name='parksettings',
            name='park',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.park', verbose_name='Автопарк'),
        ),
        migrations.AddField(
            model_name='rentinformation',
            name='partner',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.partner'),
        ),
        migrations.AddField(
            model_name='uberpaymentsorder',
            name='partner',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.partner'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='partner',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.partner'),
        ),
    ]
