# Generated by Django 3.0.7 on 2020-07-16 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rfqsite', '0011_auto_20200716_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='forecast',
            name='aeqfc',
            field=models.FloatField(default=0),
        ),
    ]
