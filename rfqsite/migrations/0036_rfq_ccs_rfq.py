# Generated by Django 3.0.7 on 2020-07-29 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rfqsite', '0035_ccs_rfq'),
    ]

    operations = [
        migrations.AddField(
            model_name='rfq',
            name='ccs_rfq',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rfqsite.CCS_RFQ'),
        ),
    ]
