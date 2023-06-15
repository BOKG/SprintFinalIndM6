from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('usuarios/', views.Usuarios.as_view(), name='usuarios'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registro/', views.Registro.as_view(), name='registro'),
    path('susignup/', views.SuSignUp.as_view(), name='registrosuper'),
]
