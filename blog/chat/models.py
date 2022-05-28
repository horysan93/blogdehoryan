from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User 
#para tener la fecha actual
from django.utils import timezone


# Para el chat partimos con 2 modelos en la app
class ThreadModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    #podemos agregar que diga si se leyó o no
    #has_unread = models.BooleanField(default=False)

class MessageModel(models.Model):
    thread = models.ForeignKey('ThreadModel', related_name='+', on_delete=models.CASCADE, blank=True, null=True)
    #usuarios que interactuan
    sender_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    receiver_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    #formato del mensaje, cuerpo, imagen, fecha y si fue leído
    body = models.CharField(max_length=1000)
    date = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)