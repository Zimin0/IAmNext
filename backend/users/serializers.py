from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    queues = serializers.PrimaryKeyRelatedField(many=True, read_only=True) # для отображения ManyToMany
    class Meta:
        model = User
        fields = ['id', 'username', 'queues']
