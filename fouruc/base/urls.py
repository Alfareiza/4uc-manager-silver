"""fouruc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path

from fouruc.base import views

app_name = 'base'

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('reset_pass', views.reset_pass, name='reset_pass'),
    path('charts', views.charts, name='charts'),
    path('login', views.login, name='login'),
    path('maps', views.maps, name='maps'),
    path('blank', views.blank, name='blank'),
    path('register', views.register, name='register'),
    path('badges', views.badges, name='badges'),
    path('breadcrumb_pagination', views.breadcrumb_pagination, name='breadcrumb_pagination'),
    path('forms', views.forms, name='forms'),
    path('button', views.button, name='button'),
    path('collapse', views.collapse, name='collapse'),
    path('icons', views.icons, name='icons'),
    path('tabs', views.tabs, name='tabs'),
    path('tables', views.tables, name='tables'),
    path('typography', views.typography, name='typography'),
]
