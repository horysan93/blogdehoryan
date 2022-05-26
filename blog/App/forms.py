from tkinter import E
from unittest.util import _MAX_LENGTH
from django import forms
import django
# Importamos librerias para la creación de usuarios!
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    #Creamos nuestra creación de usuario a nuestra medida
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)
    
    class Meta: #Esto se pone por default
        model=User 
        fields=('username', 'email', 'password1', 'password2')
        #help_texts={"username":None, "email":None,"password1":None, "password2":None}   #Hacemos que todos los textos de ayuda no estén
        help_text={k:"" for k in fields}

class UserEditForm(UserCreationForm):
    #Creamos nuestra creación de usuario a nuestra medida
    email = forms.EmailField(label = "Modificar mail")
    password1 = forms.CharField(label=" Cambiar Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)  
    #Nota lo que ponga acá lo van a poder modificar, si saco un campo, no lo podrán tocar
    #Agregar más campos
    last_name = forms.CharField(label="Modificar apellido")
    first_name = forms.CharField(label = "Modificar nombre")

    class Meta: #Esto se pone por default
        model=User 
        fields=('email', 'password1', 'password2', "last_name", "first_name")
        #help_texts={"username":None, "email":None,"password1":None, "password2":None}   #Hacemos que todos los textos de ayuda no estén
        help_text={k:"" for k in fields}

#Creamos avatarForm

class AvatarForm(forms.Form):
    avatar = forms.ImageField(label="Avatar")