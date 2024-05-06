from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.http import JsonResponse

# Create your views here.
from django.contrib.auth.models import User
from .serializers import *
class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers

    # def get_queryset(self):
    #     return User.objects.none()
    
    # @action(detail = False, methods = ['get'])
    # def superusers(self,request):
    #     queryset = User.objects.filter(is_superuser = True)

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Login user
            login(request, user)
            session_token = request.session.session_key  # Get session key
            return JsonResponse({'session_token': session_token})
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=401)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
