# Generated by Django 3.0.7 on 2020-07-06 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfqsite', '0004_auto_20200706_1627'),
    ]

    operations = [
        migrations.RenameField(
            model_name='active_rate',
            old_name='hcm',
            new_name='hmc',
        ),
        migrations.RenameField(
            model_name='active_rate',
            old_name='mca5axis',
            new_name='mca4axis',
        ),
    ]