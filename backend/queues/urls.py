from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from queues import views

urlpatterns = [
    path("queues/", views.QueueList.as_view()),
    path("queues/<int:pk>/", views.QueueDetail.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)