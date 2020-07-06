# Generated by Django 3.0.7 on 2020-07-06 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rfqsite', '0005_auto_20200706_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='active_rate',
            name='axis5',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='active_rate',
            name='bta',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='active_rate',
            name='cla',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='active_rate',
            name='duburring',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='active_rate',
            name='edm',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='active_rate',
            name='grinding',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='active_rate',
            name='hmc',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='active_rate',
            name='inspection',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='active_rate',
            name='mca3axis',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='active_rate',
            name='mca4axis',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='active_rate',
            name='tma',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='sp_rate',
            name='caa',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='sp_rate',
            name='cadmium_plating',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='sp_rate',
            name='ccc',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='sp_rate',
            name='chrome_plating',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='sp_rate',
            name='dfl',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='sp_rate',
            name='fpi',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='sp_rate',
            name='hard_anodizing',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='sp_rate',
            name='heat_treatment',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='sp_rate',
            name='mpi',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='sp_rate',
            name='paint',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='sp_rate',
            name='passivation',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='sp_rate',
            name='saa',
            field=models.FloatField(default=1),
        ),
    ]
