# Generated by Django 3.2.13 on 2022-06-03 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_questioneditors'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='is_sold',
            field=models.BooleanField(default=False),
        ),
    ]
