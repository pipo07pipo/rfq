from django.contrib import admin
from .models import RFQ, SP_Rate, Active_Rate, Part_Header, SPS, Forecast, Material, Part_Costing, MSUT, CTPP
# Register your models here.
admin.site.register(RFQ)
admin.site.register(SP_Rate)
admin.site.register(Active_Rate)
admin.site.register(Part_Header)
admin.site.register(SPS)
admin.site.register(Forecast)
admin.site.register(Material)
admin.site.register(Part_Costing)
admin.site.register(MSUT)
admin.site.register(CTPP)
