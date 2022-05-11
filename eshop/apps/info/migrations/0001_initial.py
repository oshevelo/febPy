# Generated by Django 3.2.13 on 2022-05-10 15:03

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_better_admin_arrayfield.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShopInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=85)),
                ('address', models.CharField(max_length=150)),
                ('location_longitude', models.DecimalField(decimal_places=3, max_digits=8)),
                ('location_latitude', models.DecimalField(decimal_places=3, max_digits=8)),
                ('phone_numbers', django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.CharField(max_length=16), blank=True, null=True, size=None)),
                ('emails', django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.EmailField(blank=True, max_length=150, null=True), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='ShopDaySchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(7), django.core.validators.MinValueValidator(1)])),
                ('open_hour', models.TimeField(default=datetime.time(8, 0))),
                ('close_hour', models.TimeField(default=datetime.time(17, 0))),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.shopinfo')),
            ],
        ),
    ]
