from django.shortcuts import render
from rest_framework import generics

from queues.serializers import QueueSerializer
from queues.models import Queue

class QueueDetail(generics.RetrieveAPIView):
    queryset = Queue.objects.all()
    serializer_class = QueueSerializer

class QueueList(generics.ListAPIView):
    queryset = Queue.objects.all()
    serializer_class = QueueSerializer

