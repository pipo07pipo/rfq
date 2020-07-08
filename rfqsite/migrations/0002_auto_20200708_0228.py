# Generated by Django 3.0.7 on 2020-07-07 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rfqsite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='cross_section',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='rm_d1_unit',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='rm_d2_unit',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='rm_density_unit',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='rm_l_unit',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='rm_t_unit',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='rm_w_unit',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='type',
            field=models.CharField(max_length=200, null=True),
        ),
    ]