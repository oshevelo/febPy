# Generated by Django 3.2.13 on 2022-05-13 14:03

import apps.userprofiles.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userprofiles', '0005_auto_20220510_1958'),
    ]

    operations = [
        migrations.CreateModel(
            name='OneTimeToken',
            fields=[
                ('token', models.CharField(default=apps.userprofiles.models.create_activation_token, max_length=150, primary_key=True, serialize=False)),
                ('date_of_expiry', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='token_bearer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
