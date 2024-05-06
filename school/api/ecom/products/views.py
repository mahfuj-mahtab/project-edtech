from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializers
class OrderViewSet(viewsets.ModelViewSet):
    queryset = ProductOrder.objects.all()
    serializer_class = OrderSerializers
@csrf_exempt
def orderView(request):
    if(request.method == 'POST'):
        name = request.POST['name']
        address = request.POST['address']
        phone = request.POST['phone']
        payment_method = request.POST['payment_method']
        product_id = request.POST['product_id']
        transaction_id = request.POST['transaction_id']
        quantity = request.POST['quantity']
        total_amount = request.POST['total_amount']
        order_status = request.POST['order_status']

        product = Product.objects.filter(id = product_id)
        ProductOrder(name = name,address = address,phone = phone,payment_method = payment_method,products = product,transaction_id = transaction_id,quantity = quantity,total_amount = total_amount,order_status = order_status)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)