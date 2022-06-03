# Generated by Django 3.2.13 on 2022-05-18 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='NULL', max_length=30)),
                ('descrption', models.TextField(default='NULL', max_length=1000)),
                ('upload', models.ImageField(default='NULL', upload_to='uploads/%Y/%m/%d/')),
                ('size', models.CharField(choices=[('SMALL', 'SMALL'), ('MEDIUM', 'MEDIUM'), ('BIG', 'BIG')], default='SMALL', max_length=30)),
                ('time_posted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
