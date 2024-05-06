
from django.contrib import admin
from django.urls import include, path
from api.ecom.views import *
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'users',UserViewset)


urlpatterns = [
    # path("api/", ecomhome, name = 'ecom home'),
    path("",include(router.urls)),
    path("user/login/",login_view,name = 'login view'),
]
