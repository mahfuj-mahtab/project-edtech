from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
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

class ProductOrder(models.Model):
    status = (
        ('PENDING', 'PENDING'),
        ('HOLD', 'HOLD'),
        ('DELIVERED', 'DELIVERED'),
        ('IN-DELIVERY', 'IN-DELIVERY'),
        ('CANCLED', 'CANCLED'),
    )
    payment = (
        ('BKASH', 'BKASH'),
        ('NAGAD', 'NAGAD'),
        ('ROCKET', 'ROCKET'),
        ('SSL-COMMERZ', 'SSL-COMMERZ'),
        ('CASH-ON-DELIVERY', 'CASH-ON-DELIVERY'),
      
    )
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=300)
    payment_method = models.CharField(choices=payment,max_length=300)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=100, default='0')  # Field to store transaction ID
    quantity = models.PositiveIntegerField(default=1)
    total_amount = models.CharField(max_length=50,default=0)
    order_status = models.CharField(choices=status,default='PENDING',max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.phone} - {self.name}"

