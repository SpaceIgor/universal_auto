# Generated by Django 4.1 on 2023-05-09 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('app', '0021_alter_comment_chat_id_alter_event_chat_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=255, verbose_name='Ключ')),
                ('value', models.CharField(max_length=255, verbose_name='Значення')),
                ('description', models.CharField(max_length=255, null=True, verbose_name='Опиc')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype')),
            ],
            options={
                'verbose_name': 'Сервіс',
                'verbose_name_plural': 'Сервіси',
            },
        ),
        migrations.CreateModel(
            name='BoltService',
            fields=[
                ('service_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.service')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('app.service',),
        ),
        migrations.CreateModel(
            name='NewUklonService',
            fields=[
                ('service_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.service')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('app.service',),
        ),
        migrations.CreateModel(
            name='UaGpsService',
            fields=[
                ('service_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.service')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('app.service',),
        ),
        migrations.CreateModel(
            name='UberService',
            fields=[
                ('service_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.service')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('app.service',),
        ),
    ]
