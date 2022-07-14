from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author, Category
# Create your views here.

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