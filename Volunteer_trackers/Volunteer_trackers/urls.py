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
    path('successRecovery/', auth_views.LoginView.as_view(
        template_name='authen/successR.html'), name='successRecovery'),
    path('reset/password_reset', PasswordResetView.as_view(template_name='authen/password_Rforms.html',
         email_template_name="authen/password_reset.html"), name='password_reset'),
    path('reset/password_reset_done', PasswordResetDoneView.as_view(
        template_name='authen/password_Rdone.html'), name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(
        template_name='authen/password_Rconfirms.html'), name='password_reset_confirm'),
    path('reset/done', PasswordResetCompleteView.as_view(
        template_name='authen/password_Rcomplete.html'), name='password_reset_complete'),
    path('myprofileVolun/', views.IndexView.as_view(), name='index'),
    path('myprofileVolun/update/<int:id>/',
         views.update, name='edit'),
    path('myprofileVolun/create/', views.create, name='create'),
    path('myprofileVolun/delete/<int:id>/',
         views.delete, name='delete'),
    path('myprofileVolun/deletelist/',
    views.deletelist, name='deletelist'),
    
    path('myprofileInst/', views.IndexView.as_view(), name='index'),
    path('myprofileInst/update/<int:id>/',
         views.update, name='edit'),
    path('myprofileInst/create/', views.create, name='create'),
    path('myprofileInst/delete/<int:id>/',
         views.delete, name='delete'),
    path('myprofileInst/deletelist/',
    views.deletelist, name='deletelist'),
]