from statistics import mode
from tkinter import CASCADE

from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    active = models.BooleanField(blank=False, null=False)
    description = models.CharField(max_length=500, blank=True)

    class Meta:
        verbose_name_plural = "Мероприятие"


