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
    tracker_no = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=200)
    customer_name = models.CharField(max_length=200)
    file_path = models.CharField(max_length=200, null=True, default='')
    update_date = models.DateTimeField('date publish')
    usd_thb = models.FloatField(default=35)
    current_year = models.IntegerField(default=2020)

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


class Active_Rate(models.Model):
    tracker_no = models.ForeignKey(RFQ, on_delete=models.CASCADE)
    cla = models.FloatField(default=1)
    bta = models.FloatField(default=1)
    tma = models.FloatField(default=1)
    mca3axis = models.FloatField(default=1)
    mca4axis = models.FloatField(default=1)
    hmc = models.FloatField(default=1)
    axis5 = models.FloatField(default=1)
    edm = models.FloatField(default=1)
    grinding = models.FloatField(default=1)
    deburring = models.FloatField(default=1)
    inspection = models.FloatField(default=1)


class Forecast(models.Model):
    sl_no = models.ForeignKey(Part_Header, on_delete=models.CASCADE)
    qty_per_unit = models.FloatField(default=1)
    forecast_year1 = models.FloatField(default=0)
    forecast_year2 = models.FloatField(default=0)
    forecast_year3 = models.FloatField(default=0)
    forecast_year4 = models.FloatField(default=0)
    forecast_year5 = models.FloatField(default=0)
    aeqfc = models.FloatField(default=0)

class Material(models.Model):
    sl_no = models.ForeignKey(Part_Header, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, null=True, default='')
    cross_section = models.CharField(max_length=200, null=True, default='')
    type = models.CharField(max_length=200, null=True, default='')
    quantity = models.FloatField(default=0)
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
    ebq_customer_qty = models.FloatField(null=True, default=0)
    otspsuc = models.FloatField(null=True, default=0)
    otrmac = models.FloatField(null=True, default=0)
    ottc = models.FloatField(null=True, default=0)
    ccs_quote_assumptions = models.CharField(max_length=200, default='')
    dltiw_fai = models.CharField(max_length=200, default='')
    dltiw_serial_production = models.CharField(max_length=200, default='')
    dltiw_production = models.CharField(max_length=200, default='')
    base_subcontract = models.FloatField(null=True, default=0)
    shipping_cost = models.FloatField(null=True, default=0)
    ebq_ccs_qty = models.FloatField(null=True, default=0)

class MSUT(models.Model):
    sl_no = models.ForeignKey(Part_Header, on_delete=models.CASCADE)
    cla = models.FloatField(null=True, default=0)
    bta = models.FloatField(null=True, default=0)
    tma = models.FloatField(null=True, default=0)
    mca3axis = models.FloatField(null=True, default=0)
    mca4axis = models.FloatField(null=True, default=0)
    hmc = models.FloatField(null=True, default=0)
    axis5 = models.FloatField(null=True, default=0)
    edm = models.FloatField(null=True, default=0)
    grinding = models.FloatField(null=True, default=0)

class CTPP(models.Model):
    sl_no = models.ForeignKey(Part_Header, on_delete=models.CASCADE)
    cla = models.FloatField(null=True, default=0)
    bta = models.FloatField(null=True, default=0)
    tma = models.FloatField(null=True, default=0)
    mca3axis = models.FloatField(null=True, default=0)
    mca4axis = models.FloatField(null=True, default=0)
    hmc = models.FloatField(null=True, default=0)
    axis5 = models.FloatField(null=True, default=0)
    edm = models.FloatField(null=True, default=0)
    grinding = models.FloatField(null=True, default=0)
    inspection = models.FloatField(null=True, default=0)
    deburring = models.FloatField(null=True, default=0)
    assembly = models.FloatField(null=True, default=0)
    lapping = models.FloatField(null=True, default=0)

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
    mcrftp_cla = models.FloatField(default=0)
    mcrftp_bta = models.FloatField(default=0)
    mcrftp_tma = models.FloatField(default=0)
    mcrftp_mca3axis = models.FloatField(default=0)
    mcrftp_mca4axis = models.FloatField(default=0)
    mcrftp_hmc = models.FloatField(default=0)
    mcrftp_5axis = models.FloatField(default=0)
    mcrftp_edm = models.FloatField(default=0)
    mcrftp_grinding = models.FloatField(default=0)

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
