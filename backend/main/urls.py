from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro_view, name='registro'),
    path('panel_admin/', views.panel_admin, name='panel_admin'),
    path('panel_estudiante/', views.panel_estudiante, name='panel_estudiante'),
    path('panel_acudiente/', views.panel_acudiente, name='panel_acudiente'),
    path('panel_administrativo/', views.panel_administrativo, name='panel_administrativo'),
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='main/registration/password_reset_form.html',
        email_template_name='main/registration/password_reset_email.html',
        success_url='/password_reset/done/'
    ), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='main/registration/password_reset_done.html'
    ), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='main/registration/password_reset_confirm.html',
        success_url='/reset/done/'
    ), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='main/registration/password_reset_complete.html'
    ), name='password_reset_complete'),
]
