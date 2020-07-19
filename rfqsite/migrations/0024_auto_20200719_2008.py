# Generated by Django 3.0.7 on 2020-07-19 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rfqsite', '0023_remove_mc_master_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='act_set',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='MC_Set',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msut', models.FloatField(default=0)),
                ('ctpp', models.FloatField(default=0)),
                ('act_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rfqsite.ACT_Set')),
                ('sl_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rfqsite.Part_Header')),
            ],
        ),
    ]
