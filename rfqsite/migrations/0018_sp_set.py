# Generated by Django 3.0.7 on 2020-07-18 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rfqsite', '0017_sp_master'),
    ]

    operations = [
        migrations.CreateModel(
            name='SP_Set',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spec', models.CharField(default='', max_length=200)),
                ('rate', models.FloatField(default=0)),
                ('sl_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rfqsite.Part_Header')),
                ('sp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rfqsite.SP_Master')),
            ],
        ),
    ]
