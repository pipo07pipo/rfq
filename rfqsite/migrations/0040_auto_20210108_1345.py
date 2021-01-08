# Generated by Django 3.0.7 on 2021-01-08 06:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rfqsite', '0039_delete_customer_part'),
    ]

    operations = [
        migrations.AddField(
            model_name='rfq',
            name='hyper_link',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='rfq',
            name='remark',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='rfq',
            name='remark_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='rfq',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
