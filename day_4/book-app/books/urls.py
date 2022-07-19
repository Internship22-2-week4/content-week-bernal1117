from django.urls import path
from django.db import router   #ENRUTADOR

#Django rest framework
from rest_framework.routers import DefaultRouter
#views
from .views import CategoryViewSets, BookViewSets, AuthorViewSets #llamada a las viewsets de views.py

router = DefaultRouter()
router.register(r'categories', CategoryViewSets)
router.register(r'books', BookViewSets)
router.register(r'authors', AuthorViewSets)

urlpatterns = router.urls

urlpatterns += [
  
]





"""
#Registrar esto en el proyecto urls.py, en este caso core/urls.py
urlpatterns = [
  path('', views.index, name='index'),
  path('author/<int:author_id>', views.author, name='author'),
  path('author/<int:category_id>', views.category, name='category')

]
"""