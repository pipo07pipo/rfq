# Generated by Django 3.0.7 on 2020-07-18 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfqsite', '0018_sp_set'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sps',
            name='sl_no',
        ),
        migrations.DeleteModel(
            name='SP_Rate',
        ),
        migrations.DeleteModel(
            name='SPS',
        ),
    ]
