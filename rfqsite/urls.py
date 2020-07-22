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
    path('part_info/<int:sl_no>/', views.part_info, name='part_info'),
    path('edit_part_info/<int:sl_no>/', views.edit_part_info, name='edit_part_info'),
    path('edit_part_info_confirm/', views.edit_part_info_confirm, name='edit_part_info_confirm'),
    path('edit_forecast/<int:sl_no>/', views.edit_forecast, name='edit_forecast'),
    path('edit_forecast_confirm/', views.edit_forecast_confirm, name='edit_forecast_confirm'),
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
    path('rfq_summary/<int:tracker_no>/<int:sl_no>/', views.rfq_summary2, name='summary2'),
    path('add_part_multi/<int:tracker_no>/', views.add_part_multi, name='add_part_multi'),
    path('add_part_multi_confirm/', views.add_part_multi_confirm, name='add_part_multi_confirm'),
    path('user_table/', views.user_table, name='user_table'),
    path('add_user/', views.add_user, name='add_user'),
    path('add_user_confirm/', views.add_user, name='add_user_confirm'),
    path('edit_user/<str:username>/', views.edit_user, name='edit_user'),
    path('edit_user_confirm/', views.edit_user_confirm, name='edit_user'),
    path('validate_user/', views.validate_user, name='validate_user'),
    path('remove_user/<str:username>/', views.remove_user, name='remove_user'),
    path('remove_part/<int:sl_no>/', views.remove_part, name='remove_part'),
    #####
    path('master_table/', views.master_table, name='master_table'),
    path('add_sp_master/', views.add_sp_master, name='add_sp_master'),
    path('add_sp_master_confirm/', views.add_sp_master, name='add_sp_master_confirm'),
    path('edit_sp_set/<int:sl_no>/', views.edit_sp_set, name='edit_sp_set'),
    path('select_sp_set/<int:sl_no>/', views.select_sp_set, name='select_sp_set'),
    path('select_sp_set_confirm/', views.select_sp_set_confirm, name='select_sp_set_confirm'),
    path('edit_sp_set_confirm/', views.edit_sp_set_confirm, name='edit_sp_set_confirm'),
    path('add_mc_master/', views.add_mc_master, name='add_mc_master'),
    path('add_mc_master_confirm/', views.add_mc_master, name='add_mc_master_confirm'),
    path('select_act_set/<int:tracker_no>/', views.select_act_set, name='select_act_set'),
    path('select_act_set_confirm/', views.select_act_set_confirm, name='select_act_set_confirm'),
    path('edit_act_set/<int:tracker_no>/', views.edit_act_set, name='edit_act_set'),
    path('edit_act_set_confirm/', views.edit_act_set_confirm, name='edit_act_set_confirm'),
    path('select_mc_set/<int:sl_no>/', views.select_mc_set, name='select_mc_set'),
    path('select_mc_set_confirm/', views.select_mc_set_confirm, name='select_mc_set_confirm'),
    path('edit_mc_set/<int:sl_no>/', views.edit_mc_set, name='edit_mc_set'),
    path('edit_mc_set_confirm/', views.edit_mc_set_confirm, name='edit_mc_set_confirm'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
