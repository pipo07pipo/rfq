from django.contrib import admin
from .models import SP_Master, Roles, ExtendUser,RFQ, Active_Rate, Part_Header, Forecast, Material, Part_Costing, MSUT, CTPP, Output, Hardware, Burden_Rate, SP_Set
# Register your models here.
admin.site.register(RFQ)
admin.site.register(Active_Rate)
admin.site.register(Part_Header)
admin.site.register(Forecast)
admin.site.register(Material)
admin.site.register(Part_Costing)
admin.site.register(MSUT)
admin.site.register(CTPP)
admin.site.register(Output)
admin.site.register(ExtendUser)
admin.site.register(Hardware)
admin.site.register(Burden_Rate)
admin.site.register(Roles)
admin.site.register(SP_Master)
admin.site.register(SP_Set)
