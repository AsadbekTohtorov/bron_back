from django.db import models


class Bron(models.Model):
    origin = models.CharField(max_length=255, verbose_name="Откуда")
    destination = models.CharField(max_length=255, verbose_name="Куда")
    date = models.DateField(verbose_name="Дата")
    departure_time = models.TimeField(verbose_name="Время отправления")
    arrival_time = models.TimeField(verbose_name="Время прибытия")
    admin_confirmed = models.BooleanField(default=False, verbose_name="Подтверждено администратором")
