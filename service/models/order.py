from django.contrib.auth import get_user_model
from django.db import models

from accounts.models import CustomUser
from service.models import Service
from service.models.wedding_hall import WeddingHall, Menu

User = get_user_model()


class Order(models.Model):
    IN_PROCESS = "In process"
    COMPLETED = "Completed"
    CANCELED = "Canceled"
    STATUS = (
        (IN_PROCESS, "In process"),
        (COMPLETED, "Completed"),
        (CANCELED, "Canceled")
    )

    total_price = models.PositiveIntegerField(default=0, null=True, blank=True)
    people_count = models.PositiveIntegerField(default=1, blank=True, null=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, blank=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=False)
    wedding_hall = models.ForeignKey(WeddingHall, on_delete=models.CASCADE, related_name="order", blank=False)
    service = models.ManyToManyField(Service, related_name="order")
    status = models.CharField(max_length=15, choices=STATUS, blank=True, default=IN_PROCESS)

    def __str__(self):
        return str(self.user)

    def menu_price(self):
        return self.menu.price * self.people_count

    def service_price(self):
        totl_pirce = 0
        for serv in self.service.all():
            totl_pirce += serv.price
        return (totl_pirce)

    # def total_prices(self):

