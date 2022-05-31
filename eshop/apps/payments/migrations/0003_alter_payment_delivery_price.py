# Generated by Django 3.2.13 on 2022-05-18 14:45

import apps.payments.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_auto_20220506_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='delivery_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9, validators=[apps.payments.models.Payment.validate_delivery]),
        ),
    ]