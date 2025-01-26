from rest_framework import serializers
from queues.models import Queue 

class QueueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Queue
        fields = ['id', 'title', 'max_amount', 'owner', 'members', 'slug', 'created_at', 'description', 'expire_time']
