from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone

#Importamos texto cool
from ckeditor.fields import RichTextField
from django_resized import ResizedImageField



# Create your models here.
class Juego(models.Model):
    #Creamos atributos de las reviews
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    texto = RichTextField()
    imagen = models.ImageField(upload_to = "fotos_juegos", blank = True, null=True)
    #fecha y autor
    fecha = models.DateField()
    #autor = models.CharField(max_length=50,blank=True, null=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, blank= True, null=True)
    def __str__(self):
        return self.titulo+": "+self.subtitulo+" ("+str(self.autor)+" "+str(self.fecha)+")"
        


class Noticia(models.Model):
    #Creamos atributos de las reviews
    titulo = models.CharField(max_length=50)
    #falta ponerlo luego como texto bacán
    texto = RichTextField()
    #imagen de la review
    imagen = models.ImageField()
    #fecha y autor
    fecha =  models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, blank= True, null=True)

    def __str__(self):
        return self.titulo+" ("+str(self.fecha)+")"


class Sugerencia(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank= True, null=True)

    def __str__(self):
        return self.nombre +" ("+ self.usuario+")"


class Avatar(models.Model):
    #vinculamos con el usuario que tendrá
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    #Subcarpeta de avatares que incluiremos (cambié por ResizedImageField para que si pongo cosas gigantes no explote todo)
    avatar = ResizedImageField(size=[50,50], upload_to = "avatar", blank = True, null=True)