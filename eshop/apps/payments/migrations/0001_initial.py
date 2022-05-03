# Generated by Django 3.2.13 on 2022-05-03 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_status', models.CharField(choices=[('Completed', 'Completed'), ('Processing', 'Processing'), ('Canceled', 'Canceled')], default='Processing', max_length=15)),
                ('products_price', models.DecimalField(decimal_places=2, default='0.0', max_digits=9)),
                ('delivery_price', models.DecimalField(decimal_places=2, default='0.0', max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentSystemLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raw_data', models.TextField(blank=True)),
                ('response', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]