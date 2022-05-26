"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from App import views
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name= 'inicio'),
    path('acercademi', views.acercademi, name= 'acercademi'),
    path('juegos',views.juegos, name= 'juegos'),
    path('noticias',views.noticias, name= 'noticias'),
    path('integrantes',views.integrantes, name= 'integrantes'),
    path('sugerencias',views.sugerencias, name= 'sugerencias'),
    #CRUD JUEGOS
    path('juego/list', JuegosList.as_view(), name = 'juego_listar'),
    path('juego/<pk>', JuegoDetalle.as_view(), name = 'juego_detalle'),
    path('juego/nuevo/', JuegoCreacion.as_view(), name = 'juego_crear'),
    #nuevo/ sin el / me tira error, supongo xq agrega cosas
    path('juego/editar/<pk>', JuegoEdicion.as_view(), name = 'juego_editar'),
    path('juego/borrar/<pk>', JuegoEliminacion.as_view(), name = 'juego_borrar'),
    #PATH de login, register y logout
    path('login', login_request , name = 'login'),
    path('register', register , name = 'register'),
    path('logout', LogoutView.as_view(template_name="App/logout.html") , name = 'logout'),
    #edición de perfil
    path('editarPerfil', editarPerfil, name = 'editarPerfil'),
    #agregar avatar
    path('agregarAvatar', agregarAvatar, name = 'agregarAvatar'),
]