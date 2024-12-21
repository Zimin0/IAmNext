from django.contrib import admin

from queues.models import Queue, QueueJoin

admin.site.register(Queue)
admin.site.register(QueueJoin)
