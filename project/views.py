from tokenize import Token
from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from project.models import Employee
from rest_framework import viewsets, permissions
from .serializers import  UserSerializer,RegisterSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth import authenticate


class UserViewset(viewsets.ModelViewSet):
    queryset= Employee.objects.all()
    serializer_class= UserSerializer

class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer
  
class LoginUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer



class LoginAPI(ObtainAuthToken):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        user_name=request.data['user_name']
        password=request.data['password']
        user=authenticate(request,username=user_name, password=password)
        print(user)
        token=Token.objects.create(user=user)
        return Response({
            'body': 'login successful',
            "token": token.key
        })   
