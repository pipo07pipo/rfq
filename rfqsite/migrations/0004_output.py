# Generated by Django 3.0.7 on 2020-07-12 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rfqsite', '0003_auto_20200712_1833'),
    ]

    operations = [
        migrations.CreateModel(
            name='Output',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ccs_ewp', models.FloatField(default=0)),
                ('sl_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rfqsite.Part_Header')),
            ],
        ),
    ]
