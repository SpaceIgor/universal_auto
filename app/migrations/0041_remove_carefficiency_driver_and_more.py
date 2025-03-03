# Generated by Django 4.1 on 2023-08-15 12:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0040_reporttelegrampayments_order_report_tg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carefficiency',
            name='driver',
        ),
        migrations.RemoveField(
            model_name='rentinformation',
            name='driver_name',
        ),
        migrations.RemoveField(
            model_name='rentinformation',
            name='rent_time',
        ),
        migrations.AddField(
            model_name='fleetorder',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Cтворено'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='accepted_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Час прийняття замовленя'),
        ),
        migrations.AddField(
            model_name='order',
            name='finish_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Час завершення замовлення'),
        ),
        migrations.AddField(
            model_name='rentinformation',
            name='report_from',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата звіту'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rentinformation',
            name='road_time',
            field=models.DurationField(blank=True, null=True, verbose_name='Час в дорозі'),
        ),
        migrations.AlterField(
            model_name='fleetorder',
            name='finish_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Час завершення замовлення'),
        ),
        migrations.AlterField(
            model_name='fleetorder',
            name='from_address',
            field=models.CharField(max_length=255, null=True, verbose_name='Місце посадки'),
        ),
        migrations.AlterField(
            model_name='order',
            name='chat_id_client',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Ідентифікатор чату клієнта'),
        ),
        migrations.AlterField(
            model_name='order',
            name='client_message_id',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Ідентифікатор повідомлення клієнта'),
        ),
        migrations.AlterField(
            model_name='order',
            name='driver_message_id',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Ідентифікатор повідомлення водія'),
        ),
        migrations.CreateModel(
            name='DriverEfficiency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_from', models.DateField(verbose_name='Звіт за')),
                ('total_kasa', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Всього каса')),
                ('total_orders', models.IntegerField(default=0, verbose_name='Всього замовлень')),
                ('accept_percent', models.IntegerField(default=0, verbose_name='Відсоток прийнятих замовлень')),
                ('average_price', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Середній чек, грн')),
                ('mileage', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Пробіг, км')),
                ('efficiency', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Ефективність, грн/км')),
                ('driver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.driver', verbose_name='Водій авто')),
                ('partner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.partner', verbose_name='Партнер')),
            ],
            options={
                'verbose_name': 'Ефективність водія',
                'verbose_name_plural': 'Ефективність водіїв',
            },
        ),
    ]
