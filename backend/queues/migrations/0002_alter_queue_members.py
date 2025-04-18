# Generated by Django 4.2.16 on 2025-01-26 15:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('queues', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queue',
            name='members',
            field=models.ManyToManyField(related_name='queues', through='queues.QueueJoin', to=settings.AUTH_USER_MODEL),
        ),
    ]
