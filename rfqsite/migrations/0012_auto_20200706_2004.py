# Generated by Django 3.0.7 on 2020-07-06 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfqsite', '0011_auto_20200706_2001'),
    ]

    operations = [
        migrations.RenameField(
            model_name='part_costing',
            old_name='target_prize',
            new_name='target_price',
        ),
    ]
