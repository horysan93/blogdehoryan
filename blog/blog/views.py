from django.http import HttpResponse
from django.shortcuts import render

#from App.forms import *
from App.models import *


# Create your views here.
#vamos acambiar inicio
def inicio(request):
    return render(request,"App/inicio.html")

