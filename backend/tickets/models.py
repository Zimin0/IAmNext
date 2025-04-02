from django.db import models

class Ticket(models.Model):
    """ Заявки и обратная связь. """
    name = models.CharField(max_length=30, verbose_name="Имя")
    email = models.EmailField(max_length=150, verbose_name="Электронная почта")
    message = models.TextField(max_length=2000, verbose_name="Сообщение")

    def __str__(self):
        return f"{self.name} ({self.email})"

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

