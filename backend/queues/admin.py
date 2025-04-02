from django.contrib import admin

from queues.models import Queue, QueueJoin

admin.site.register(Queue)

@admin.register(QueueJoin)
class QueueJoinAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "queue", "available_positions", "position")
    readonly_fields = ("available_positions",)
