# Generated by Django 3.2.13 on 2022-05-13 01:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discount',
            old_name='user_point',
            new_name='user_points',
        ),
    ]