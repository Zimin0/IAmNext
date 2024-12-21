# Generated by Django 4.2.16 on 2024-12-01 14:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Queue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок-название очереди')),
                ('max_amount', models.IntegerField(verbose_name='Максимальное число участников')),
                ('slug', models.CharField(editable=False, max_length=50, verbose_name='Слаг для URL')),
                ('description', models.TextField(blank=True, default='', max_length=50)),
                ('expire_time', models.DateTimeField(blank=True, null=True, verbose_name='Время закрытия очереди.')),
            ],
        ),
        migrations.CreateModel(
            name='QueueJoin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.DateTimeField(auto_created=True, verbose_name='Когда присоединился?')),
                ('position', models.IntegerField(verbose_name='Позиция в очереди.')),
                ('queue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='queues.queue')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='queue',
            name='members',
            field=models.ManyToManyField(through='queues.QueueJoin', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='queue',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='owned_queues', to=settings.AUTH_USER_MODEL, verbose_name='Владелец'),
        ),
    ]
