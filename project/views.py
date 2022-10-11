from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from project.models import Employee
from .serializers import  UserSerializer,RegisterSerializer,LoginSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics


class UserViewset(viewsets.ModelViewSet):
    queryset= Employee.objects.all()
    serializer_class= UserSerializer

class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer
  
class LoginUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer
