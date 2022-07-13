from django.urls import path
from . import views # .  para importar clases o paquetes dentro de la misma carpeta, sino se llama por el nombre 

urlpatterns = [
    path('hello/', views.index, name='index'), #ruta, archivo.nombre, nombrequeledaremos
]