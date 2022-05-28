from tkinter import E
from unittest.util import _MAX_LENGTH
from django import forms
import django
# Importamos librerias para la creación de usuarios!
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ThreadForm(forms.Form):
      username = forms.CharField(label='', max_length=100)
      
class MessageForm(forms.Form):
      message = forms.CharField(label='', max_length=1000)


