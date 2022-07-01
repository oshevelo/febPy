# Generated by Django 3.2.13 on 2022-06-17 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='source',
            field=models.CharField(choices=[('cart', 'cart'), ('catalog', 'catalog'), ('discount', 'discount'), ('info', 'info'), ('notifications', 'notifications'), ('order', 'order'), ('payment', 'payment'), ('product', 'product'), ('shipment', 'shipment'), ('user_profile', 'user_profile'), ('other_source', 'other_source')], default='other_source', max_length=200),
        ),
    ]
