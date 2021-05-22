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
    path('', views.dashboard, name='dashboard'),
    path('reset_pass.html', views.reset_pass, name='reset_pass'),
    path('charts.html', views.charts, name='charts'),
    path('login.html', views.login, name='login'),
    path('maps.html', views.maps, name='maps'),
    path('page_not_found_fourzerothree.html', views.page_not_found_fourzerothree, name='page_not_found_fourzerothree'),
    path('page_not_found_fourzerofour.html', views.page_not_found_fourzerofour, name='page_not_found_fourzerofour'),
    path('page_bad_request.html', views.page_bad_request, name='page_bad_request'),
    path('blank.html', views.blank, name='blank'),
    path('register.html', views.register, name='register'),
    path('badges.html', views.badges, name='badges'),
    path('breadcrumb_pagination.html', views.breadcrumb_pagination, name='breadcrumb_pagination'),
    path('forms.html', views.forms, name='forms'),
    path('button.html', views.button, name='button'),
    path('collapse.html', views.collapse, name='collapse'),
    path('icons.html', views.icons, name='icons'),
    path('tabs.html', views.tabs, name='tabs'),
    path('tables.html', views.tables, name='tables'),
    path('typography.html', views.typography, name='typography'),
]
