from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro_view, name='registro'),
    path('panel_admin/', views.panel_admin, name='panel_admin'),
    path('panel_estudiante/', views.panel_estudiante, name='panel_estudiante'),
    path('panel_acudiente/', views.panel_acudiente, name='panel_acudiente'),
    path('panel_administrativo/', views.panel_administrativo, name='panel_administrativo'),
]
