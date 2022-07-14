from django.urls import path
from . import views


#Registrar esto en el proyecto urls.py, en este caso core/urls.py
urlpatterns = [
  path('', views.index, name='index'),
  path('author/<int:author_id>', views.author, name='author'),
  path('author/<int:category_id>', views.category, name='category')

]