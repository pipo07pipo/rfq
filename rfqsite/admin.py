from django.contrib import admin
from .models import MC_Master, SP_Master, Roles, ExtendUser,RFQ, Part_Header, Forecast, Material, Part_Costing, Output, Hardware, Burden_Rate, SP_Set, ACT_Set, MC_Set, CCS_RFQ
# Register your models here.
admin.site.register(RFQ)
admin.site.register(Part_Header)
admin.site.register(Forecast)
admin.site.register(Material)
admin.site.register(Part_Costing)
admin.site.register(Output)
admin.site.register(ExtendUser)
admin.site.register(Hardware)
admin.site.register(Burden_Rate)
admin.site.register(Roles)
admin.site.register(SP_Master)
admin.site.register(SP_Set)
admin.site.register(MC_Master)
admin.site.register(ACT_Set)
admin.site.register(MC_Set)
admin.site.register(CCS_RFQ)
