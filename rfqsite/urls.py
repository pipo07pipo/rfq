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
    path('edit_active_rate_confirm/', views.edit_active_rate, name='projects'),
    ###
    path('add_child/', views.add_child, name='projects'),
    path('edit_ctpp/', views.edit_ctpp, name='projects'),
    path('edit_forecast/', views.edit_forecast, name='projects'),
    path('edit_material/', views.edit_material, name='projects'),
    path('edit_msut/', views.edit_msut, name='projects'),
    path('edit_part_costing/', views.edit_part_costing, name='projects'),
    path('edit_part_info/', views.edit_part_info, name='projects'),
    path('edit_sp_rate/', views.edit_sp_rate, name='projects'),
    path('edit_sps/', views.edit_sps, name='projects'),
    path('part_info/', views.part_info, name='projects'),
]
