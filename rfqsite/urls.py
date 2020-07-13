from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('rfq_table/', views.rfq_table, name='rfq_table'),
    path('part_table/<int:tracker_no>/', views.parts, name='part_table'),
    path('add_part/<int:tracker_no>/', views.add_part, name='add_part'),
    path('add_part_confirm/', views.add_part_confirm, name='add_part_confirm'),
    path('edit_rfq/<int:tracker_no>/', views.edit_rfq, name='edit_rfq'),
    path('edit_rfq_confirm/', views.edit_rfq_confirm, name='edit_rfq_confirm'),
    path('edit_active_rate/<int:tracker_no>/', views.edit_active_rate, name='edit_active_rate'),
    path('edit_active_rate_confirm/', views.edit_active_rate_confirm, name='edit_active_rate_confirm'),
    path('edit_sp_rate/<int:sl_no>/', views.edit_sp_rate, name='edit_sp_rate'),
    path('edit_sp_rate_confirm/', views.edit_sp_rate_confirm, name='edit_sp_rate_confirm'),
    path('part_info/<int:sl_no>/', views.part_info, name='part_info'),
    path('edit_part_info/<int:sl_no>/', views.edit_part_info, name='edit_part_info'),
    path('edit_part_info_confirm/', views.edit_part_info_confirm, name='edit_part_info_confirm'),
    path('edit_forecast/<int:sl_no>/', views.edit_forecast, name='edit_forecast'),
    path('edit_forecast_confirm/', views.edit_forecast_confirm, name='edit_forecast_confirm'),
    path('edit_ctpp/<int:sl_no>/', views.edit_ctpp, name='edit_ctpp'),
    path('edit_ctpp_confirm/', views.edit_ctpp_confirm, name='edit_ctpp_confirm'),
    path('edit_sps/<int:sl_no>/', views.edit_sps, name='edit_sps'),
    path('edit_sps_confirm/', views.edit_sps_confirm, name='edit_sps_confirm'),
    path('edit_msut/<int:sl_no>/', views.edit_msut, name='edit_msut'),
    path('edit_msut_confirm/', views.edit_msut_confirm, name='edit_msut_confirm'),
    path('edit_part_costing/<int:sl_no>/', views.edit_part_costing, name='edit_part_costing'),
    path('edit_part_costing_confirm/', views.edit_part_costing_confirm, name='edit_part_costing_confirm'),
    path('add_child/<int:sl_no>/', views.add_child, name='add_child'),
    path('add_child_confirm/', views.add_child_confirm, name='add_child_confirm'),
    path('edit_material/<int:sl_no>/', views.edit_material, name='edit_material'),
    path('edit_material_confirm/', views.edit_material_confirm, name='edit_material_confirm'),
    path('edit_material_remove/<int:sl_no>/', views.edit_material_remove, name='edit_material_remove'),
    path('edit_burden_rate/<int:sl_no>/', views.edit_burden_rate, name='edit_burden_rate'),
    path('edit_burden_rate_confirm/', views.edit_burden_rate_confirm, name='edit_burden_rate_confirm'),
    path('edit_hardware/<int:sl_no>/', views.edit_hardware, name='edit_hardware'),
    path('edit_hardware_confirm/', views.edit_hardware_confirm, name='edit_hardware_confirm'),
    path('data_collect/', views.data_collect, name='data_collect'),
    path('rfq_summary/<int:tracker_no>/', views.rfq_summary, name='summary'),
    path('add_part_multi/<int:tracker_no>/', views.add_part_multi, name='add_part_multi'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
