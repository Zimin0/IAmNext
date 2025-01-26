from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Queue(models.Model):
    """ Очередь из пользователей. """

    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="Заголовок-название очереди")
    max_amount = models.IntegerField(null=False, blank=False, verbose_name="Максимальное число участников")
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="owned_queues", verbose_name="Владелец", null=True)
    members = models.ManyToManyField(User, through="QueueJoin", related_name="queues")
    slug = models.CharField(max_length=50, null=False, blank=False, editable=False, verbose_name="Слаг для URL")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Была создана")
    description = models.TextField(max_length=50, null=False, blank=True, default="")
    expire_time = models.DateTimeField(null=True, blank=True, verbose_name="Время закрытия очереди.")

    def get_taken_positions(self) -> set:
        """ Возвращает номера занятых позиций. """
        taken_positions = set()
        for queue_join in QueueJoin.objects.filter(queue=self):
            taken_positions.add(queue_join.position)
        return taken_positions

    def get_free_positions(self) -> set:
        """ Возвращает номера свободных позиций. """
        taken_positions = self.get_taken_positions()
        all_positions = set(range(1, self.max_amount + 1))
        
        return all_positions - taken_positions

    def __str__(self):
        return f"{self.title}"

class QueueJoin(models.Model):
    """ Промежуточная модель для ManyToManyField Queue и User. """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    queue = models.ForeignKey(Queue, on_delete=models.CASCADE)
    when = models.DateTimeField(auto_created=True, blank=False, null=False, verbose_name="Когда присоединился?")
    position = models.IntegerField(null=False, blank=False, verbose_name="Позиция в очереди.")

    def __str__(self):
        return f'"{self.user}" в "{self.queue}"'
    
    def clean(self):
        if self.position < 1:
            raise ValidationError({"position": "Позиция не может быть меньше 1."})
        if self.position > self.queue.max_amount:
            raise ValidationError({"position": f"Максимальная длина этой очереди: {self.queue.max_amount}."})

        if self.position in self.queue.get_taken_positions():
            raise ValidationError({"position": f"Это место в очереди уже занято. Вот свободные места: {self.queue.get_free_positions()}"})

        # проверка на то, что ползователь уже состоит в очереди

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args,**kwargs)