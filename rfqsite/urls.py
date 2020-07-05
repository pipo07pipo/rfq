from django.urls import path
from . import views

urlpatterns = [
    path('rfq_table/', views.rfq_table, name='rfq_table'),
    path('projects/', views.projects, name='projects'),
    path('part_table/<int:tracker_no>/', views.parts, name='parts'), 
    path('add_child/', views.add_child, name='projects'),
    path('add_part/<int:tracker_no>/', views.add_part, name='projects'), 
    path('add_part_confirm', views.add_part_confirm, name='projects'), 
    path('edit_active_rate/', views.edit_active_rate, name='projects'),
    path('edit_ctp/', views.edit_ctp, name='projects'),
    path('edit_forecast/', views.edit_forecast, name='projects'),
    path('edit_material/', views.edit_material, name='projects'),
    path('edit_mst/', views.edit_mst, name='projects'),
    path('edit_part_costing/', views.edit_part_costing, name='projects'),
    path('edit_part_info/', views.edit_part_info, name='projects'),
    path('edit_rfq/', views.edit_rfq, name='projects'),
    path('edit_special_process_rate/', views.edit_special_process_rate, name='projects'),
    path('edit_sps/', views.edit_sps, name='projects'),
    path('part_info/', views.part_info, name='projects'),
]
