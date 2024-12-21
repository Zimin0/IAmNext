from django.db import models
from django.contrib.auth.models import User

class Queue(models.Model):
    """ Очередь из пользователей. """

    def __str__(self):
        return f"{self.title}"

    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="Заголовок-название очереди")
    max_amount = models.IntegerField(null=False, blank=False, verbose_name="Максимальное число участников")
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="owned_queues", verbose_name="Владелец", null=True)
    members = models.ManyToManyField(User, through="QueueJoin")
    slug = models.CharField(max_length=50, null=False, blank=False, editable=False, verbose_name="Слаг для URL")
    description = models.TextField(max_length=50, null=False, blank=True, default="")
    expire_time = models.DateTimeField(null=True, blank=True, verbose_name="Время закрытия очереди.")


class QueueJoin(models.Model):
    """ Промежуточная модель для  ManyToManyField Queue и User. """

    def __str__(self):
        return f"{self.user} в {self.queue}"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    queue = models.ForeignKey(Queue, on_delete=models.CASCADE)
    when = models.DateTimeField(auto_created=True, blank=False, null=False, verbose_name="Когда присоединился?")
    position = models.IntegerField(null=False, blank=False, verbose_name="Позиция в очереди.")
