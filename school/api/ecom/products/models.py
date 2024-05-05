from django.db import models

# Create your models here.
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='upload/products/')
    parent = models.ForeignKey('self',on_delete=models.CASCADE, null=True,blank=True,related_name='childern_category')
    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='upload/products/')
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    brand = models.ForeignKey('Brand',on_delete=models.CASCADE)
    stock_quantity = models.PositiveIntegerField(default=0)
    featureImage = models.ImageField(upload_to='upload/products/')
    image1 = models.ImageField(upload_to='upload/products/', null=True, blank=True)
    image2 = models.ImageField(upload_to='upload/products/', null=True, blank=True)
    image3 = models.ImageField(upload_to='upload/products/', null=True, blank=True)
    sku = models.CharField(max_length=50, unique=True)
    weight = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    length = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    width = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    height = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name
