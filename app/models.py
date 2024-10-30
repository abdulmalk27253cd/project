from django.db import models

# Create your models here.
import datetime
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
#@daverobb2011
    class Meta:
        verbose_name_plural = 'categories'
    
    
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    
    
    def __str__(self):
        return f'{self.fist_name} {self.last_name}' 
    
    
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    categoory = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='product/')

    def __str__(self):
        return self.name

class Oreder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    phone = models.CharField(max_length=20, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)

    def __str__(self):
        return {self.product}
