from django.urls import path
from . import views

app_name = 'module_engine'

urlpatterns = [
    path('', views.module_list, name='module_list'),
    path('install/<int:module_id>/', views.install_module, name='install_module'),
    path('uninstall/<int:module_id>/', views.uninstall_module, name='uninstall_module'),
    path('upgrade/<int:module_id>/', views.upgrade_module, name='upgrade_module'),
] 