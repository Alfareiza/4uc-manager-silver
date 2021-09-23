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

from fouruc.manager import views

app_name = 'manager'

urlpatterns = [
    #  Gerenciamento de contas
    path('', views.contas, name='contas'),
    path('detalhe/<slug:slug>/', views.conta_detalhe, name='conta_detalhe'),

    #  Atualiza Conta
    path(r'update/<slug:slug>/all', views.update_all_data_account, name='update_data_account'),
    path(r'update/<slug:slug>/players', views.update_players, name='update_players'),
    path(r'update/<slug:slug>/playlists', views.update_playlists, name='update_playlists'),
    path(r'update/<slug:slug>/medias', views.update_medias, name='update_medias'),
    path(r'update/<slug:slug>/categories', views.update_categories, name='update_categories'),

    #  Deleta conta
    path(r'delete/<slug:slug>/', views.delete, name='delete'),

    #  Relatórios
    path('playlogs/', views.playlogs, name='playlogs'),
    path('relatorios/', views.solicitar_relatorio, name='solicitar_relatorio'),

]
