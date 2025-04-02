from django.shortcuts import render
from rest_framework import generics

from tickets.models import Ticket
from tickets.serializers import TicketSerializer

class TicketDetail(generics.RetrieveAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class TicketList(generics.ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class TicketCreate(generics.CreateAPIView):
    """Эндпоинт для создания тикетов"""
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer