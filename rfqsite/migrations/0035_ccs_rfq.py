# Generated by Django 3.0.7 on 2020-07-29 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rfqsite', '0034_rfq_customer_file_path'),
    ]

    operations = [
        migrations.CreateModel(
            name='CCS_RFQ',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('ccs_tracker_no', models.CharField(default='', max_length=200)),
                ('description', models.CharField(default='', max_length=200)),
                ('customer_name', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
