# Generated by Django 3.2.13 on 2022-06-17 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_question_is_sold'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='length',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]