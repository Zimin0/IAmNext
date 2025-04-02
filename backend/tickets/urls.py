from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from tickets import views

urlpatterns = [
    path("tickets/", views.TicketList.as_view()),
    path("tickets/<int:pk>/", views.TicketDetail.as_view()),
    path("tickets/create", views.TicketCreate.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)