# Generated by Django 5.0.6 on 2024-06-03 04:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camera', '0003_remove_shipment_price_remove_shipment_total_weight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipment',
            name='additional_details',
        ),
    ]
