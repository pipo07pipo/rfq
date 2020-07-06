from django.db import models

# Create your models here.

class RFQ(models.Model):
    tracker_no = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=200)
    customer_name = models.CharField(max_length=200)
    file_path = models.CharField(max_length=200)
    update_date = models.DateTimeField('date publish')

class SP_Rate(models.Model):
    tracker_no = models.ForeignKey(RFQ, on_delete=models.CASCADE)
    fpi = models.FloatField(default=1)
    mpi = models.FloatField(default=1)
    passivation = models.FloatField(default=1)
    caa = models.FloatField(default=1)
    saa = models.FloatField(default=1)
    hard_anodizing = models.FloatField(default=1)
    ccc = models.FloatField(default=1)
    dfl = models.FloatField(default=1)
    paint = models.FloatField(default=1)
    cadmium_plating = models.FloatField(default=1)
    chrome_plating = models.FloatField(default=1)
    heat_treatment = models.FloatField(default=1)

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

class Part_Header(models.Model):
    sl_no = models.AutoField(primary_key=True)
    tracker_no = models.ForeignKey(RFQ, on_delete=models.CASCADE)
    no = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    level = models.IntegerField()
    program = models.CharField(max_length=200)
    parent_sl_no = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    file_path = models.CharField(max_length=200)
    image_path = models.CharField(max_length=200)

class SPS(models.Model):
    sl_no = models.ForeignKey(Part_Header, on_delete=models.CASCADE)
    surface_treatment = models.CharField(max_length=200)
    ht = models.CharField(max_length=200)
    fpi = models.CharField(max_length=200)
    mpi = models.CharField(max_length=200)
    primer = models.CharField(max_length=200)
    solid_film = models.CharField(max_length=200)
    pmr = models.CharField(max_length=200)

class Forecast(models.Model):
    sl_no = models.ForeignKey(Part_Header, on_delete=models.CASCADE)
    qty_per_unit = models.FloatField(default=1)
    forecast_year1 = models.FloatField(default=100)
    forecast_year2 = models.FloatField(default=100)
    forecast_year3 = models.FloatField(default=100)
    forecast_year4 = models.FloatField(default=100)
    forecast_year5 = models.FloatField(default=100)
    forecast_current_year = models.DateTimeField('date publish')

class Material(models.Model):
    sl_no = models.ForeignKey(Part_Header, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    cross_section = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    quantity = models.FloatField(default=1)
    rm_density = models.FloatField(null=True)
    rm_density_unit = models.CharField(max_length=200)
    rm_d1 = models.FloatField(null=True)
    rm_d1_unit = models.CharField(max_length=10)
    rm_d2 = models.FloatField(null=True)
    rm_d2_unit = models.CharField(max_length=10)
    rm_t = models.FloatField(null=True)
    rm_t_unit = models.CharField(max_length=10)
    rm_w = models.FloatField(null=True)
    rm_w_unit = models.CharField(max_length=10)
    rm_l = models.FloatField(null=True)
    rm_l_unit = models.CharField(max_length=10)
    rm_total_weight = models.FloatField(null=True)

class Part_Costing(models.Model):
    sl_no = models.ForeignKey(Part_Header, on_delete=models.CASCADE)
    hardware_supplier = models.CharField(max_length=200)
    base_material_price = models.FloatField(null=True)
    material_supplier = models.CharField(max_length=200)
    material_shipping_cost = models.FloatField(null=True)
    nre_amortizing_cost = models.FloatField(null=True)
    target_prize = models.FloatField(null=True)
    ebq_customer_qty = models.FloatField(null=True)
    otspsuc = models.FloatField(null=True)
    otrmac = models.FloatField(null=True)
    ottc = models.FloatField(null=True)
    ccs_quote_assumptions = models.CharField(max_length=200)
    dltiw_fai = models.CharField(max_length=200)
    dltiw_serial_production = models.CharField(max_length=200)
    dltiw_production = models.CharField(max_length=200)
class MSUT(models.Model):
    sl_no = models.ForeignKey(Part_Header, on_delete=models.CASCADE)
    cla = models.FloatField(null=True)
    bta = models.FloatField(null=True)
    tma = models.FloatField(null=True)
    mca3axis = models.FloatField(null=True)
    mca4axis = models.FloatField(null=True)
    hmc = models.FloatField(null=True)
    axis5 = models.FloatField(null=True)
    edm = models.FloatField(null=True)
    grinding = models.FloatField(null=True)

class CTPP(models.Model):
    sl_no = models.ForeignKey(Part_Header, on_delete=models.CASCADE)
    cla = models.FloatField(null=True)
    bta = models.FloatField(null=True)
    tma = models.FloatField(null=True)
    mca3axis = models.FloatField(null=True)
    mca4axis = models.FloatField(null=True)
    hmc = models.FloatField(null=True)
    axis5 = models.FloatField(null=True)
    edm = models.FloatField(null=True)
    grinding = models.FloatField(null=True)
    inspection = models.FloatField(null=True)
    deburring = models.FloatField(null=True)
    assembly = models.FloatField(null=True)
    lapping = models.FloatField(null=True)
