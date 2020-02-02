"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('index',views.gethome),
    path('home',views.home),
    path('register_investor',views.r_investor),
    path('register_user',views.r_user),
    path('get_idea',views.getidea),
    path('profile_user',views.getprofile),
    path('add_idea',views.addidea),
    path('watchlist',views.watchlist),
    path('add_tolist',views.tolist),
    path('crm',views.details),
]
