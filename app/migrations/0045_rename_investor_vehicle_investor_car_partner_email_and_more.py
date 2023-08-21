# Generated by Django 4.1 on 2023-08-21 13:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0044_vehicle_investor_percentage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicle',
            old_name='investor',
            new_name='investor_car',
        ),
        migrations.AddField(
            model_name='partner',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Електрона пошта'),
        ),
        migrations.AddField(
            model_name='partner',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name="Ім'я"),
        ),
        migrations.AddField(
            model_name='partner',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Прізвище'),
        ),
        migrations.AddField(
            model_name='partner',
            name='phone_number',
            field=models.CharField(blank=True, max_length=13, null=True, verbose_name='Номер телефона'),
        ),
        migrations.AddField(
            model_name='partner',
            name='role',
            field=models.CharField(choices=[('CLIENT', 'Client'), ('DRIVER', 'Driver'), ('DRIVER_MANAGER', 'Driver manager'), ('SERVICE_STATION_MANAGER', 'Service station manager'), ('SUPPORT_MANAGER', 'Support manager'), ('OWNER', 'Owner'), ('INVESTOR', 'Investor')], default='OWNER', max_length=25),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('CLIENT', 'Client'), ('DRIVER', 'Driver'), ('DRIVER_MANAGER', 'Driver manager'), ('SERVICE_STATION_MANAGER', 'Service station manager'), ('SUPPORT_MANAGER', 'Support manager'), ('OWNER', 'Owner'), ('INVESTOR', 'Investor')], default='CLIENT', max_length=25),
        ),
        migrations.CreateModel(
            name='VehicleSpendings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Сума')),
                ('category', models.CharField(choices=[('FUEL', 'Паливо'), ('SERVICE', 'Сервісне обслуговування'), ('REPAIR', 'Ремонт'), ('WASHING', 'Мийка'), ('OTHER', 'Інше')], max_length=255, verbose_name='Категорія витрат')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Опис')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Створено')),
                ('vehicle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.vehicle', verbose_name='Автомобіль')),
            ],
            options={
                'verbose_name': 'Витрата',
                'verbose_name_plural': 'Витрати',
            },
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True, verbose_name="Ім'я")),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Прізвище')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Електрона пошта')),
                ('phone_number', models.CharField(blank=True, max_length=13, null=True, verbose_name='Номер телефона')),
                ('chat_id', models.CharField(blank=True, max_length=10, null=True, verbose_name='Індетифікатор чата')),
                ('role', models.CharField(choices=[('CLIENT', 'Client'), ('DRIVER', 'Driver'), ('DRIVER_MANAGER', 'Driver manager'), ('SERVICE_STATION_MANAGER', 'Service station manager'), ('SUPPORT_MANAGER', 'Support manager'), ('OWNER', 'Owner'), ('INVESTOR', 'Investor')], default='DRIVER_MANAGER', max_length=25)),
                ('partner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.partner', verbose_name='Партнер')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Користувач')),
            ],
            options={
                'verbose_name': 'Менеджер',
                'verbose_name_plural': 'Менеджери',
            },
        ),
        migrations.CreateModel(
            name='Investor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True, verbose_name="Ім'я")),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Прізвище')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Електрона пошта')),
                ('phone_number', models.CharField(blank=True, max_length=13, null=True, verbose_name='Номер телефона')),
                ('role', models.CharField(choices=[('CLIENT', 'Client'), ('DRIVER', 'Driver'), ('DRIVER_MANAGER', 'Driver manager'), ('SERVICE_STATION_MANAGER', 'Service station manager'), ('SUPPORT_MANAGER', 'Support manager'), ('OWNER', 'Owner'), ('INVESTOR', 'Investor')], default='INVESTOR', max_length=25)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('vehicle', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.vehicle', verbose_name='Автомобіль')),
            ],
        ),
        migrations.AlterField(
            model_name='driver',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.manager', verbose_name='Менеджер водіїв'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.manager', verbose_name='Менеджер авто'),
        ),
        migrations.DeleteModel(
            name='DriverManager',
        ),
    ]
