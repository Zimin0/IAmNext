from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics

from users.serializers import UserSerializer

# List - для коллекции, Detail - для одного объекта
class UserDetail(generics.RetrieveAPIView): #  только для чтения (через get) 
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
