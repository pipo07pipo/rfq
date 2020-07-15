from django.contrib import admin
from .models import Role, ExtendUser,RFQ, SP_Rate, Active_Rate, Part_Header, SPS, Forecast, Material, Part_Costing, MSUT, CTPP, Output, Hardware, Burden_Rate
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
admin.site.register(Output)
admin.site.register(ExtendUser)
admin.site.register(Hardware)
admin.site.register(Burden_Rate)
admin.site.register(Role)
