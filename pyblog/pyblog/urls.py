"""pyblog URL Configuration

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
from django.urls import path
from app_pyblog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('submit', views.submit_login),
    path('logout/', views.logout_user),
    path('cadastro/', views.cadastrar_user),
    path('cadastro/submit', views.submit_cadastro_user),
    path('minha_pagina/', views.minha_pagina),
    path('escrever_publicacao/', views.escrever_publicacao),
    path('publicacao/<titulo_publicacao>/', views.publicacao, name='publicacao'),
    path('editar_perfil/', views.editar_perfil),
    path('editar_perfil/submit', views.submit_editar_perfil),
]
