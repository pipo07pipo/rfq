from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Roles(models.Model):
    permission = models.IntegerField(default=2)
    type = models.CharField(max_length=200,default='')

class ExtendUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Roles, on_delete=models.SET_NULL, null=True)

class RFQ(models.Model):
    tracker_no = models.AutoField(primary_key=True)
    ccs_tracker_no = models.CharField(max_length=200, default='')
    description = models.CharField(max_length=200)
    customer_name = models.CharField(max_length=200)
    file_path = models.CharField(max_length=200, default='')
    update_date = models.DateTimeField('date publish')
    usd_thb = models.FloatField(default=35)
    current_year = models.IntegerField(default=2020)
    last_generate = models.DateTimeField('date publish', null=True)
    customer_file_path = models.CharField(max_length=200, default='')

class Customer_Part(models.Model):
    tracker_no = models.ForeignKey(RFQ, on_delete=models.CASCADE)
    sl_no = models.IntegerField(default=0)
    no = models.CharField(max_length=10, default='')
    name = models.CharField(max_length=200, default='')
    program = models.CharField(max_length=200, default='')
    current_year = models.IntegerField(default=2020)
    forecast_year1 = models.IntegerField(default=0)
    forecast_year2 = models.IntegerField(default=0)
    forecast_year3 = models.IntegerField(default=0)
    forecast_year4 = models.IntegerField(default=0)
    forecast_year5 = models.IntegerField(default=0)
    description = models.CharField(max_length=200, null=True, default='')
    material_cost = models.FloatField(default=0)
    surface_treatment_cost = models.FloatField(default=0)
    hardware_cost = models.FloatField(default=0)
    total_manufacturing_cost = models.FloatField(default=0)
    ccs_ewp = models.FloatField(default=0)
    ebq_customer_qty = models.IntegerField(null=True, default=0)
    aeqfc = models.IntegerField(default=0)
    ottc = models.FloatField(null=True, default=0)
    ccs_quote_assumptions = models.CharField(max_length=200, default='')
    dltiw_fai = models.CharField(max_length=200, default='')
    dltiw_serial_production = models.CharField(max_length=200, default='')
    dltiw_production = models.CharField(max_length=200, default='')

class Part_Header(models.Model):
    sl_no = models.AutoField(primary_key=True)
    tracker_no = models.ForeignKey(RFQ, on_delete=models.CASCADE)
    no = models.CharField(max_length=10, default='')
    name = models.CharField(max_length=200, default='')
    level = models.IntegerField()
    program = models.CharField(max_length=200, default='')
    parent_sl_no = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    file_path = models.CharField(max_length=200, default='')
    image_path = models.CharField(max_length=200, default='')
    type = models.CharField(max_length=50, default='Part')

class Forecast(models.Model):
    sl_no = models.ForeignKey(Part_Header, on_delete=models.CASCADE)
    qty_per_unit = models.IntegerField(default=1)
    forecast_year1 = models.IntegerField(default=0)
    forecast_year2 = models.IntegerField(default=0)
    forecast_year3 = models.IntegerField(default=0)
    forecast_year4 = models.IntegerField(default=0)
    forecast_year5 = models.IntegerField(default=0)
    aeqfc = models.IntegerField(default=0)

class Material(models.Model):
    sl_no = models.ForeignKey(Part_Header, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, null=True, default='')
    cross_section = models.CharField(max_length=200, null=True, default='')
    type = models.CharField(max_length=200, null=True, default='')
    quantity = models.IntegerField(default=0)
    rm_density = models.FloatField(null=True, default=0)
    rm_density_unit = models.CharField(max_length=200, null=True)
    rm_d1 = models.FloatField(null=True, default=0)
    rm_d1_unit = models.CharField(max_length=10, null=True, default='')
    rm_d2 = models.FloatField(null=True, default=0)
    rm_d2_unit = models.CharField(max_length=10, null=True, default='')
    rm_t = models.FloatField(null=True, default=0)
    rm_t_unit = models.CharField(max_length=10, null=True, default='')
    rm_w = models.FloatField(null=True, default=0)
    rm_w_unit = models.CharField(max_length=10, null=True, default='')
    rm_l = models.FloatField(null=True, default=0)
    rm_l_unit = models.CharField(max_length=10, null=True, default='')
    rm_total_weight = models.FloatField(null=True, default=0)
    fpwp = models.FloatField(null=True, default=0)
    armwpp = models.FloatField(null=True, default=0)
    base_material_price = models.FloatField(null=True, default=0)
    supplier = models.CharField(max_length=200, default='')
    shipping_cost = models.FloatField(null=True, default=0)

class Hardware(models.Model):
    sl_no = models.ForeignKey(Part_Header, on_delete=models.CASCADE)
    supplier = models.CharField(max_length=200, default='')
    price = models.FloatField(null=True, default=0)
    description = models.CharField(max_length=200, default='')
    qty = models.FloatField(default=0)

class Part_Costing(models.Model):
    sl_no = models.ForeignKey(Part_Header, on_delete=models.CASCADE)
    total_nre_cost = models.FloatField(null=True, default=0)
    target_price = models.FloatField(null=True, default=0)
    ebq_customer_qty = models.IntegerField(null=True, default=0)
    otspsuc = models.FloatField(null=True, default=0)
    otrmac = models.FloatField(null=True, default=0)
    ottc = models.FloatField(null=True, default=0)
    ccs_quote_assumptions = models.CharField(max_length=200, default='')
    dltiw_fai = models.CharField(max_length=200, default='')
    dltiw_serial_production = models.CharField(max_length=200, default='')
    dltiw_production = models.CharField(max_length=200, default='')
    base_subcontract = models.FloatField(null=True, default=0)
    shipping_cost = models.FloatField(null=True, default=0)
    ebq_ccs_qty = models.IntegerField(null=True, default=0)

class Burden_Rate(models.Model):
    subcontract = models.FloatField(default=1)
    sl_no = models.ForeignKey(Part_Header, on_delete=models.CASCADE)
    material = models.FloatField(default=1)
    hardware = models.FloatField(default=1)
    sp = models.FloatField(default=1)

class Output(models.Model):
    sl_no = models.ForeignKey(Part_Header, on_delete=models.CASCADE)
    ccs_ewp = models.FloatField(default=0)
    total_cost = models.FloatField(default=0)
    mtl_cost = models.FloatField(default=0)
    spl_process_cost = models.FloatField(default=0)
    total_hardware_cost = models.FloatField(default=0)
    total_machine_cost = models.FloatField(default=0)
    material_burden_cost = models.FloatField(default=0)
    sp_burden_cost = models.FloatField(default=0)
    hardware_burden_cost = models.FloatField(default=0)
    material_cost = models.FloatField(default=0)
    surface_treatment_cost = models.FloatField(default=0)
    hardware_cost = models.FloatField(default=0)
    total_manufacturing_cost = models.FloatField(default=0)

class SP_Master(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200,default='')

class SP_Set(models.Model):
    sl_no = models.ForeignKey(Part_Header, on_delete=models.CASCADE)
    sp_id = models.ForeignKey(SP_Master, on_delete=models.CASCADE)
    spec = models.CharField(max_length=200,default='')
    rate = models.FloatField(default=0)

class MC_Master(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200,default='')

class ACT_Set(models.Model):
    id = models.AutoField(primary_key=True)
    tracker_no = models.ForeignKey(RFQ, on_delete=models.CASCADE)
    mc_id = models.ForeignKey(MC_Master, on_delete=models.CASCADE)
    rate = models.FloatField(default=0)

class MC_Set(models.Model):
    sl_no = models.ForeignKey(Part_Header, on_delete=models.CASCADE)
    act_id = models.ForeignKey(ACT_Set, on_delete=models.CASCADE)
    msut = models.FloatField(default=0)
    ctpp = models.FloatField(default=0)
    mcrftp = models.FloatField(default=0)
