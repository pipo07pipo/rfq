# Generated by Django 3.0.7 on 2020-07-27 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rfqsite', '0033_auto_20200727_0334'),
    ]

    operations = [
        migrations.AddField(
            model_name='rfq',
            name='customer_file_path',
            field=models.CharField(default='', max_length=200),
        ),
    ]
