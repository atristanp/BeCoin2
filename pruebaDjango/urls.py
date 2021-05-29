from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('noticias', views.news),
    path('recursos', views.resources),
    path('simulador', views.simulator),
    path('register', views.register),
    path('login', views.loginPage),
    path('logout', views.logoutUser),
]