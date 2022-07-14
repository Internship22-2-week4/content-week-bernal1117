from unicodedata import category
from django.test import TestCase
from books.models import Category, Book, Author
# from .models import Category, Book, Author    Se puede hacer asi tambien  

# Podemos testear models y views

class CategoryModelTest(TestCase):
  """
  Test category model
  """
  def setUp(self):
    """
    Set up non-modified objects used by all test methods
    """
    Category.objects.create(name='test', description='test', status=True) #Aqui configuramos lo que queremos testear: objetos, variables, funciones

  def test_category_name_is_not_blank(self): #Aqui llamamos lo que configuramos
    """
    Test category name is not blank
    """
    category = Category.objects.get(id=1)
    self.assertEqual(category.name, 'test')
