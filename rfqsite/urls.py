from django.urls import path
from . import views

urlpatterns = [
    path('rfq_table/', views.rfq_table, name='rfq_table'),
    path('part_table/<int:tracker_no>/', views.parts, name='parts'),
    path('add_part/<int:tracker_no>/', views.add_part, name='projects'),
    path('add_part_confirm/', views.add_part_confirm, name='projects'),
    path('edit_rfq/<int:tracker_no>/', views.edit_rfq, name='projects'),
    path('edit_rfq_confirm/', views.edit_rfq_confirm, name='projects'),
    path('edit_active_rate/<int:tracker_no>/', views.edit_active_rate, name='projects'),
    path('edit_active_rate_confirm/', views.edit_active_rate_confirm, name='projects'),
    path('edit_sp_rate/<int:tracker_no>/', views.edit_sp_rate, name='projects'),
    path('edit_sp_rate_confirm/', views.edit_sp_rate_confirm, name='projects'),
    path('part_info/<int:sl_no>/', views.part_info, name='projects'),
    path('edit_part_info/<int:sl_no>/', views.edit_part_info, name='projects'),
    path('edit_part_info_confirm/', views.edit_part_info_confirm, name='projects'),
    path('edit_forecast/<int:sl_no>/', views.edit_forecast, name='projects'),
    path('edit_forecast_confirm/', views.edit_forecast_confirm, name='projects'),
    path('edit_ctpp/<int:sl_no>/', views.edit_ctpp, name='projects'),
    path('edit_ctpp_confirm/', views.edit_ctpp_confirm, name='projects'),
    path('edit_sps/<int:sl_no>/', views.edit_sps, name='projects'),
    path('edit_sps_confirm/', views.edit_sps_confirm, name='projects'),
    path('edit_msut/<int:sl_no>/', views.edit_msut, name='projects'),
    path('edit_msut_confirm/', views.edit_msut_confirm, name='projects'),
    path('edit_part_costing/<int:sl_no>/', views.edit_part_costing, name='projects'),
    path('edit_part_costing_confirm/', views.edit_part_costing_confirm, name='projects'),
    path('add_child/<int:sl_no>/', views.add_child, name='projects'),
    path('add_child_confirm/', views.add_child_confirm, name='projects'),
    path('edit_material/<int:sl_no>/', views.edit_material, name='projects'),
    path('edit_material_confirm/', views.edit_material_confirm, name='projects'),

]
