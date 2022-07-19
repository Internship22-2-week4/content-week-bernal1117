#from django.shortcuts import render
#from django.http import HttpResponse

#Django rest framework 
from rest_framework.views import Response
from rest_framework import viewsets

from .serializers import CategorySerializer, BookSerializer, AuthorSerializer

#models
from .models import Book, Author, Category

class CategoryViewSets(viewsets.ModelViewSet):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer

class BookViewSets(viewsets.ModelViewSet):
  queryset = Book.objects.all()
  serializer_class = BookSerializer

class AuthorViewSets(viewsets.ModelViewSet):
  queryset = Author.objects.all()
  serializer_class = AuthorSerializer















"""
def index(request):
  books = Book.objects.all()
  for book in books:
    print(book.title, book.author.first_name, book.category.name)

  return render(request, 'index.html', { #Recibe el path del html en este caso esta en templates
    "books_list": books
  })
  #return HttpResponse('App book')

def author(request, author_id):
  author = Author.objects.get(id=author_id)
  return render(request, 'author.html', { #Recibe el path del html en este caso esta en templates
    "author": author
  })

  #return HttpResponse(f'<h1>Author id: {author_id} </h1>' )

def category(request, category_id):
  return HttpResponse(f'<h1>Category id: {category_id} </h1>') 
"""