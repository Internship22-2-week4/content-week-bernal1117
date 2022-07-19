
from django.db import models

# Creando tablas por asi decirlo o SCHEMAS
class Author(models.Model):    
  #Al heredar models de Django nos da automaticamente un ID por eso no lo declaro aca
  first_name = models.CharField(max_length=50) # ORM de Django
  last_name = models.CharField(max_length=50)
  uri_image = models.CharField(max_length=200)
  status = models.BooleanField(default=True)

  def __str__(self):
    return f'{self.first_name} - {self.last_name}' # Para poder recuperar datos

class Category(models.Model):    
  name = models.CharField(max_length=50) # PRIMERO VAN LAS CLASES QUE NO TIENEN DEPENDENCIAS DE OTRAS
  description = models.CharField(max_length=200)
  status = models.BooleanField(default=True)

  def __str__(self):
    return f'{self.name} - {self.description}' # Para poder recuperar datos y los datos que llamemos metodo 3 de serializers.py


class Book(models.Model):    
  title = models.CharField(max_length=50) 
  image = models.CharField(max_length=200)
  isbn = models.CharField(max_length=13)
  status = models.BooleanField(default=True)
  author = models.ForeignKey(Author, on_delete=models.CASCADE) #Recibe la clase Author para poder leer su id
  category = models.ForeignKey(Category, on_delete=models.CASCADE) #Como en SQL borra los registros que tengan conexion en forma de cascada

  # Con el metodo 3 aqui se modifica lo que se va a mostrar en el formulario desde serializers.py
  def __str__(self):
    return f'{self.title} - {self.isbn} - {self.author.first_name}' # Para poder recuperar datos

#Author.objects.all()
#Author.objects.create('atributos de la clase o modelo')
#Author.objects.filter(firs_name='John ') 

"""def __str__(self):
    return self.name
  
  def __unicode__(self):
    return self.name"""