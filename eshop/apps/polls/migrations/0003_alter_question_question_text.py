# Generated by Django 3.2.7 on 2022-04-19 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_choice_choice_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=20),
        ),
    ]
