from django.db import models

from service.models.events import Event


class WeddingHall(models.Model):
    name = models.CharField(max_length=250, blank=False, null=False)
    address = models.CharField(max_length=250, blank=False, null=False)
    cite = models.CharField(max_length=250, blank=False, null=False)
    image = models.FileField(upload_to='media/', blank=True, null=True)
    event = models.ManyToManyField(Event, related_name="wedding_hall")


class Menu(models.Model):
    type = models.CharField(max_length=250, blank=False, null=False)
    price = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    wedding_hall = models.ForeignKey(WeddingHall, on_delete=models.CASCADE, related_name="menus")

    def save(self, *args, **kwargs):
        super(Menu, self).save(*args, **kwargs)

    def __str__(self):
        return self.type


class MenuItem(models.Model):
    name = models.CharField(max_length=250, blank=False, null=False)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="menu_items")

    def __str__(self):
        return self.name