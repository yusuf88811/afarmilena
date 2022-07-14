from django.db import models

from service.models.events import Event


class Service(models.Model):
    name = models.CharField(max_length=250, blank=False, null=False)
    type = models.CharField(max_length=250, blank=False, null=False)
    price = models.PositiveIntegerField(max_length=250, blank=True)
    image = models.ImageField(upload_to="images/", blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)
# from services.models.restoran import EvantModel
#
# class Category(models.Model):
#     name = models.CharField(max_length=30)
#
#     def __str__(self):
#         return self.name
#
# class ServiceModel(models.Model):
#     event_type = models.ForeignKey(EvantModel, on_delete=models.CASCADE)
#     category_type = models.ForeignKey(Category, on_delete=models.CASCADE)
#     name = models.CharField(max_length=30)
#     type = models.CharField(max_length=30)
#     price = models.PositiveIntegerField(default=0)
#     image = models.ImageField(upload_to='service/', blank=True, null=True)
#     file = models.FileField(upload_to='service/', blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#
#     def __str__(self):
#         return str(self.category_type)