from rest_framework import serializers
from queues.models import Queue 

class QueueSerializer(serializers.ModelSerializer):
    member_count = serializers.SerializerMethodField()

    class Meta:
        model = Queue
        fields = ['id', 'title', 'max_amount', 'owner', 'members', 'slug', 'created_at', 'description', 'expire_time', 'member_count']

    def get_member_count(self, obj):
        return obj.members.count()
