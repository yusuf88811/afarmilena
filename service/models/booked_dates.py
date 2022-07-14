from django.db import models
from service.models.wedding_hall import WeddingHall


class BookedDates(models.Model):
    date = models.DateField(blank=False, null=False)
    wedding_hall = models.ForeignKey(WeddingHall, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('date', 'wedding_hall')
        verbose_name_plural = "Забронированные даты"
