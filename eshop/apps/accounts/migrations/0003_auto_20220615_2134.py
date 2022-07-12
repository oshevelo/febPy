# Generated by Django 3.2.13 on 2022-06-15 21:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_rename_points_rating_pointcount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='discount',
            field=models.FloatField(default=0.05, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='discount',
            name='prev_count',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='pointcount',
            name='points',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='rating',
            name='percentile',
            field=models.FloatField(default=100, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]