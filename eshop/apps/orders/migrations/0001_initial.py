# Generated by Django 3.2.13 on 2022-07-01 22:55

import apps.orders.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shipments', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_type', models.CharField(choices=[('NEW', 'New'), ('PAID', 'Paid'), ('DELIVERED', 'Delivered'), ('CANCELED', 'Canceled'), ('COMPLETED', 'Completed')], default='New', max_length=20)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Last updated')),
                ('value', models.DecimalField(decimal_places=2, max_digits=7, validators=[apps.orders.models.Order.validate_order_value])),
                ('shipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='shipments.shipments')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Customer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='orders.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='products.product')),
            ],
        ),
    ]
