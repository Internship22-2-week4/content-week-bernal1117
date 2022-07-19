from dataclasses import fields
from pyexpat import model
from unicodedata import category, name
from rest_framework import serializers

from .models import Book, Author, Category


#Esto viene de rest_framework y ayuda a la conversion de diccionarios a JSON usa tambien los modelos que teniamos
class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Author
    fields = '__all__' #Son los datos que vamos a mostrar en este caso todos __all__

class BookSerializer(serializers.ModelSerializer):
  """ # Metodo 1 para mostrar datos de la relacion entre las tablas
  category = CategorySerializer()
  author = AuthorSerializer() 
  """
  """
  # Metodo 2 para mostar datos de la relacion entre las tablas
  category = serializers.SlugRelatedField(
    many=False,
    read_only=True,
    slug_field='name'
  ) 
  author = serializers.SlugRelatedField(
    many=False,
    read_only=True,
    slug_field='first_name'
  )
"""
  # Metodo 3 para mostrar datos de la relacion entre las tablas
  author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
  category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
  class Meta:
    model = Book
    fields = '__all__' 
    #exclude = ('id','author','category') #Que muestre todo menos los datos especificados
    #fields = ['title', 'author', 'category'] #Solo muestra los datos especificados
  
  def to_representation(self, instance):  #Con esto mostramos lo que necesitemos
    return {
      'id': instance.id,
      'title': instance.title,
      'image': instance.image,
      'isbn': instance.isbn,
      'author': {
        'first_name': instance.author.first_name,
        'last_name': instance.author.last_name
      },
      'category': {
        'id': instance.category.id,
        'name': instance.category.name,
        'description': instance.category.description
      }
    }
