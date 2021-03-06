# Generated by Django 3.0.7 on 2020-07-19 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rfqsite', '0021_mc_master'),
    ]

    operations = [
        migrations.CreateModel(
            name='ACT_Set',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.FloatField(default=0)),
                ('mc_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rfqsite.MC_Master')),
                ('tracker_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rfqsite.RFQ')),
            ],
        ),
    ]
