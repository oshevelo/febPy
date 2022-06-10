# Generated by Django 3.2.13 on 2022-05-28 22:41

# Generated by Django 3.2 on 2022-05-17 14:09


from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(verbose_name='Created')),
                ('order_type', models.CharField(choices=[('NEW', 'New'), ('PAID', 'Paid'), ('DELIVERED', 'Delivered'), ('CANCELLED', 'Cancelled'), ('COMPLETED', 'Completed')], default='New', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, verbose_name='Full name')),
                ('address_line1', models.CharField(max_length=512, verbose_name='Address line 1')),
                ('address_line2', models.CharField(max_length=512, verbose_name='Address line 2')),
                ('post_code', models.CharField(max_length=8, verbose_name='Postcode')),
                ('city', models.CharField(max_length=56, verbose_name='City')),
                ('country', models.CharField(max_length=56, verbose_name='Country')),
            ],
            options={
                'verbose_name': 'Shipping Address',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.shippingaddress'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
