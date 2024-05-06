
from django.contrib import admin
from django.urls import include, path
from api.ecom.views import *
from rest_framework.routers import DefaultRouter
from .products.views import *

router = DefaultRouter()
router.register(r'products',ProductViewSet)
router.register(r'category',CategoryViewSet)
router.register(r'brand',BrandViewSet)

urlpatterns = [
    # path("api/", ecomhome, name = 'ecom home'),
    path("",include(router.urls)),
]
