# Generated by Django 3.2.13 on 2022-05-25 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0005_auto_20220525_1748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='payment_status',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='payment_system',
        ),
    ]