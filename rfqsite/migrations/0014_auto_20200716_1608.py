# Generated by Django 3.0.7 on 2020-07-16 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfqsite', '0013_auto_20200716_1603'),
    ]

    operations = [
        migrations.RenameField(
            model_name='part_costing',
            old_name='ddp_shipping_cost',
            new_name='shipping_cost',
        ),
    ]
