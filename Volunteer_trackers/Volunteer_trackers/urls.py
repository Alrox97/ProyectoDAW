from django.conf.urls import include
from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from dawi import views
"""
    Este módulo es el encargado de definir de las rutas de la aplicación.
"""
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='authen/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
     path('myprofileVolun/', auth_views.LoginView.as_view(template_name='institutions/myprofileVolun.html'), name='myprofileVolun'),
]