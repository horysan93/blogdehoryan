
from django.urls import path
from chat import views
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('inbox', ListThreads.as_view(), name = 'inbox'),
    path('inbox/create-thread', CreateThread.as_view(), name = 'create-thread'),
    path('inbox/<int:pk>', ThreadView.as_view(), name = 'thread'),
    path('inbox/<int:pk>/create-message', CreateMessage.as_view(), name = 'create-message'),
]