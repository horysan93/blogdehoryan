from django.http import HttpResponse
from django.shortcuts import render

#from App.forms import *
from App.models import *
from App.forms import *

#importaciones para la CRUB
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

#Importaciones para el login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout

#Importaciones para limitar acceso a la información
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required





#vamos acambiar inicio
#@login_required
def inicio(request):
    juegos_recientes = Juego.objects.order_by('-fecha')[:1]
    noticias_recientes = Noticia.objects.order_by('-fecha')[:1]
  
    if request.user.is_authenticated:
        avatar=Avatar.objects.filter(user=request.user)
        if not(avatar):
            return render(request,"App/inicio.html",{'juegos_recientes':juegos_recientes, 'noticias_recientes':noticias_recientes})        
        return render(request,"App/inicio.html",{'url':avatar[0].avatar.url, 'juegos_recientes':juegos_recientes, 'noticias_recientes':noticias_recientes})
    return render(request,"App/inicio.html",{'juegos_recientes':juegos_recientes, 'noticias_recientes':noticias_recientes})



def acercademi(request):
    return render(request,"App/acercademi.html")

# Creamos paginas para cada clase que utilizamos:  
def juegos(request):
    return render(request,"App/juegos.html")

def noticias(request):
    return render(request,"App/noticias.html")

def integrantes(request):
    return render(request, "App/integrantes.html")

def sugerencias(request):
    return render(request, "App/sugerencias.html")


#---------
# ADMIN REQUIREMENTS
#--------
from django.contrib.auth.mixins import UserPassesTestMixin

class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

#---------------------------------------------
# CRUD VARIABLES
#---------------------------------------------
class JuegosList(ListView): 
    #El LoginRequiredMixin debe ir primero para que lo tome
    model = Juego
    template_name= 'App/juego_list.html'

class JuegoDetalle(DetailView):    #mostrar 
    model = Juego
    template_name = 'App/juego_detalle.html'

class JuegoCreacion(LoginRequiredMixin, CreateView):   #Crear 
    model = Juego
    success_url = reverse_lazy("juego_listar")  #Fijamos la url que buscará cuando sale bien
    #Campos que tiene que mostrar
    fields=['titulo','subtitulo','categoria','texto','imagen','fecha','autor']       


class JuegoEdicion(LoginRequiredMixin, UpdateView):    #editar
    model = Juego
    success_url = reverse_lazy("juego_listar") 
    fields=['titulo','subtitulo','categoria','texto','imagen','fecha','autor']     



class JuegoEliminacion(AdminRequiredMixin, DeleteView):  #eliminar
    model = Juego
    success_url = reverse_lazy("juego_listar")  #Fijamos la url que buscará cuando sale bien
    #Campos que tiene que mostrar
    fields=['titulo','subtitulo','categoria','texto','imagen','fecha','autor']     



#----------------------------------------------------
# CREAMOS CLASE PARA EL LOGIN
#----------------------------------------------------
def login_request(request):

    if request.method == "POST":
        formulario = AuthenticationForm(request=request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get("username") #usuario -> el ingresado por el teclado
            clave=formulario.cleaned_data.get("password")
            user = authenticate(username=usuario, password=clave)   #User que trae de la base si lo anterior está correcto
            
            if user is not None:
                login(request, user)        #si es correcto logea y entrega render que lleva la inicio más mensaje
                return render(request, "App/inicio.html", {"usuario":usuario, "mensaje": ", bienvenido nuevamente"})
            else:
                return render(request, "App/login.html",{"formulario":formulario, "mensaje":" usuario Incorrecto :C"})

        #Si el formulario no es valido:
        else:
            return render(request, "App/login.html",{"formulario":formulario,"mensaje":"Formulario inválido :C"})
    else:
        formulario=AuthenticationForm()
        return render(request,"App/login.html", {"formulario":formulario})

# Registrar nuevos usuarios
def register(request):
    if request.method == "POST":

        #form = UserCreationForm(request.POST) reemplazamos por el que utilizaremos!
        form = UserRegisterForm(request.POST)
        if form.is_valid():

            username=form.cleaned_data["username"]
            form.save()
            return render(request, "App/inicio.html", {"mensaje": f"Usuario: {username} creado de manera exitosa"})
        else:
            return render(request, "App/inicio.html", {"mensaje": "No se pudo crear el usuario"})
    
    else:
        form = UserRegisterForm()
        return render(request,"App/register.html", {"form":form})

#Debe estar logeada la persona (o sería rancio editar el perfil de alguien que no está XD)
@login_required
def editarPerfil(request):
    usuario=request.user

    if request.method == 'POST':
        formulario=UserEditForm(request.POST, instance=usuario)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            usuario.email=informacion['email']
            usuario.password1=informacion['password1']
            usuario.password2=informacion['password2']
            usuario.save()

            return render(request, 'App/inicio.html', {'usuario':usuario, 'mensaje':'Cambios guardados'})
    else:
        formulario=UserEditForm(instance=usuario)
    return render(request, 'App/editarPerfil.html', {'formulario':formulario, 'usuario':usuario.username})

@login_required
def agregarAvatar(request):
    user = User.objects.get(username=request.user)
    if request.method == "POST":
        formulario=AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():
            avatar=Avatar(user=user, avatar=formulario.cleaned_data["avatar"])
            avatar.save()
            return render(request, "App/inicio.html", {'usuario':user, 'mensaje': "AVATAR AGREGADO"})
    else:
        formulario=AvatarForm()
    return render(request, 'App/agregarAvatar.html', {'formulario':formulario, 'usuario':user})


