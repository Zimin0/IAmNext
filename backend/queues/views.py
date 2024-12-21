from django.shortcuts import render
from rest_framework import generics

from queues.serializers import UserSerializer
from django.contrib.auth.models import User


class UserList(generics.ListAPIView): #  только для чтения (через get) 
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

