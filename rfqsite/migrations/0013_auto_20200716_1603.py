# Generated by Django 3.0.7 on 2020-07-16 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfqsite', '0012_forecast_aeqfc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='part_costing',
            old_name='nre_amortizing_cost',
            new_name='total_nre_cost',
        ),
    ]