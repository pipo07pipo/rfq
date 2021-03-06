# Generated by Django 3.0.7 on 2020-07-11 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Part_Header',
            fields=[
                ('sl_no', models.AutoField(primary_key=True, serialize=False)),
                ('no', models.CharField(default='', max_length=10)),
                ('name', models.CharField(default='', max_length=200)),
                ('level', models.IntegerField()),
                ('program', models.CharField(default='', max_length=200)),
                ('file_path', models.CharField(default='', max_length=200)),
                ('image_path', models.CharField(default='', max_length=200)),
                ('parent_sl_no', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rfqsite.Part_Header')),
            ],
        ),
        migrations.CreateModel(
            name='RFQ',
            fields=[
                ('tracker_no', models.IntegerField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=200)),
                ('customer_name', models.CharField(max_length=200)),
                ('file_path', models.CharField(default='', max_length=200, null=True)),
                ('update_date', models.DateTimeField(verbose_name='date publish')),
            ],
        ),
        migrations.CreateModel(
            name='SPS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surface_treatment', models.CharField(default='', max_length=200)),
                ('ht', models.CharField(default='', max_length=200)),
                ('fpi', models.CharField(default='', max_length=200)),
                ('mpi', models.CharField(default='', max_length=200)),
                ('primer', models.CharField(default='', max_length=200)),
                ('solid_film', models.CharField(default='', max_length=200)),
                ('pmr', models.CharField(default='', max_length=200)),
                ('sl_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rfqsite.Part_Header')),
            ],
        ),
        migrations.CreateModel(
            name='SP_Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fpi', models.FloatField(default=1)),
                ('mpi', models.FloatField(default=1)),
                ('passivation', models.FloatField(default=1)),
                ('caa', models.FloatField(default=1)),
                ('saa', models.FloatField(default=1)),
                ('hard_anodizing', models.FloatField(default=1)),
                ('ccc', models.FloatField(default=1)),
                ('dfl', models.FloatField(default=1)),
                ('paint', models.FloatField(default=1)),
                ('cadmium_plating', models.FloatField(default=1)),
                ('chrome_plating', models.FloatField(default=1)),
                ('heat_treatment', models.FloatField(default=1)),
                ('sl_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rfqsite.Part_Header')),
            ],
        ),
        migrations.AddField(
            model_name='part_header',
            name='tracker_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rfqsite.RFQ'),
        ),
        migrations.CreateModel(
            name='Part_Costing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nre_amortizing_cost', models.FloatField(default=0, null=True)),
                ('target_price', models.FloatField(default=0, null=True)),
                ('ebq_customer_qty', models.FloatField(default=0, null=True)),
                ('otspsuc', models.FloatField(default=0, null=True)),
                ('otrmac', models.FloatField(default=0, null=True)),
                ('ottc', models.FloatField(default=0, null=True)),
                ('ccs_quote_assumptions', models.CharField(default='', max_length=200)),
                ('dltiw_fai', models.CharField(default='', max_length=200)),
                ('dltiw_serial_production', models.CharField(default='', max_length=200)),
                ('dltiw_production', models.CharField(default='', max_length=200)),
                ('base_subcontract', models.FloatField(default=0, null=True)),
                ('subcontract_shipping_cost', models.FloatField(default=0, null=True)),
                ('ddp_shipping_cost', models.FloatField(default=0, null=True)),
                ('ddp_usd', models.FloatField(default=0, null=True)),
                ('sl_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rfqsite.Part_Header')),
            ],
        ),
        migrations.CreateModel(
            name='MSUT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cla', models.FloatField(default=0, null=True)),
                ('bta', models.FloatField(default=0, null=True)),
                ('tma', models.FloatField(default=0, null=True)),
                ('mca3axis', models.FloatField(default=0, null=True)),
                ('mca4axis', models.FloatField(default=0, null=True)),
                ('hmc', models.FloatField(default=0, null=True)),
                ('axis5', models.FloatField(default=0, null=True)),
                ('edm', models.FloatField(default=0, null=True)),
                ('grinding', models.FloatField(default=0, null=True)),
                ('sl_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rfqsite.Part_Header')),
            ],
        ),
        migrations.CreateModel(
            name='Material2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fpwp', models.FloatField(default=0, null=True)),
                ('armwpp', models.FloatField(default=0, null=True)),
                ('base_material_price', models.FloatField(default=0, null=True)),
                ('supplier', models.CharField(default='', max_length=200)),
                ('shipping_cost', models.FloatField(default=0, null=True)),
                ('sl_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rfqsite.Part_Header')),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='', max_length=200, null=True)),
                ('cross_section', models.CharField(default='', max_length=200, null=True)),
                ('type', models.CharField(default='', max_length=200, null=True)),
                ('quantity', models.FloatField(default=0)),
                ('rm_density', models.FloatField(null=True)),
                ('rm_density_unit', models.CharField(max_length=200, null=True)),
                ('rm_d1', models.FloatField(default=0, null=True)),
                ('rm_d1_unit', models.CharField(default='', max_length=10, null=True)),
                ('rm_d2', models.FloatField(default=0, null=True)),
                ('rm_d2_unit', models.CharField(default='', max_length=10, null=True)),
                ('rm_t', models.FloatField(default=0, null=True)),
                ('rm_t_unit', models.CharField(default='', max_length=10, null=True)),
                ('rm_w', models.FloatField(default=0, null=True)),
                ('rm_w_unit', models.CharField(default='', max_length=10, null=True)),
                ('rm_l', models.FloatField(default=0, null=True)),
                ('rm_l_unit', models.CharField(default='', max_length=10, null=True)),
                ('rm_total_weight', models.FloatField(default=0, null=True)),
                ('sl_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rfqsite.Part_Header')),
            ],
        ),
        migrations.CreateModel(
            name='Hardware',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier', models.CharField(default='', max_length=200)),
                ('price', models.FloatField(default=0, null=True)),
                ('description', models.CharField(default='', max_length=200)),
                ('qty', models.FloatField(default=0)),
                ('sl_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rfqsite.Part_Header')),
            ],
        ),
        migrations.CreateModel(
            name='Forecast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty_per_unit', models.FloatField(default=1)),
                ('forecast_year1', models.FloatField(default=0)),
                ('forecast_year2', models.FloatField(default=0)),
                ('forecast_year3', models.FloatField(default=0)),
                ('forecast_year4', models.FloatField(default=0)),
                ('forecast_year5', models.FloatField(default=0)),
                ('forecast_current_year', models.DateTimeField(verbose_name='date publish')),
                ('sl_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rfqsite.Part_Header')),
            ],
        ),
        migrations.CreateModel(
            name='CTPP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cla', models.FloatField(default=0, null=True)),
                ('bta', models.FloatField(default=0, null=True)),
                ('tma', models.FloatField(default=0, null=True)),
                ('mca3axis', models.FloatField(default=0, null=True)),
                ('mca4axis', models.FloatField(default=0, null=True)),
                ('hmc', models.FloatField(default=0, null=True)),
                ('axis5', models.FloatField(default=0, null=True)),
                ('edm', models.FloatField(default=0, null=True)),
                ('grinding', models.FloatField(default=0, null=True)),
                ('inspection', models.FloatField(default=0, null=True)),
                ('deburring', models.FloatField(default=0, null=True)),
                ('assembly', models.FloatField(default=0, null=True)),
                ('lapping', models.FloatField(default=0, null=True)),
                ('sl_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rfqsite.Part_Header')),
            ],
        ),
        migrations.CreateModel(
            name='Burden_Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.FloatField(default=1)),
                ('hardware', models.FloatField(default=1)),
                ('subcontract', models.FloatField(default=1)),
                ('sp', models.FloatField(default=1)),
                ('sl_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rfqsite.Part_Header')),
            ],
        ),
        migrations.CreateModel(
            name='Active_Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cla', models.FloatField(default=1)),
                ('bta', models.FloatField(default=1)),
                ('tma', models.FloatField(default=1)),
                ('mca3axis', models.FloatField(default=1)),
                ('mca4axis', models.FloatField(default=1)),
                ('hmc', models.FloatField(default=1)),
                ('axis5', models.FloatField(default=1)),
                ('edm', models.FloatField(default=1)),
                ('grinding', models.FloatField(default=1)),
                ('deburring', models.FloatField(default=1)),
                ('inspection', models.FloatField(default=1)),
                ('tracker_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rfqsite.RFQ')),
            ],
        ),
    ]
