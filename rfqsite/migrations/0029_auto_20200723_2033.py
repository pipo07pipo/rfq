# Generated by Django 3.0.7 on 2020-07-23 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rfqsite', '0028_auto_20200723_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rfq',
            name='file_path',
            field=models.CharField(default='', max_length=200),
        ),
    ]
