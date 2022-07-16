from django.db import models

from accounts.models import CustomUser
from service.models.order import Order


class History(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    query = models.CharField(max_length=250, blank=True, null=True)
    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
