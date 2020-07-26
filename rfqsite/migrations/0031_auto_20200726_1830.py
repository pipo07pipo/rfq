# Generated by Django 3.0.7 on 2020-07-26 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rfqsite', '0030_auto_20200726_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='output',
            name='hardware_cost',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='output',
            name='material_cost',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='output',
            name='surface_treatment_cost',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='output',
            name='total_manufacturing_cost',
            field=models.FloatField(default=0),
        ),
    ]
