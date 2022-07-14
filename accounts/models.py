from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=13, null=False, blank=True, unique=True)
    cite = models.CharField(max_length=50, null=False, blank=False)
    wedding_date = models.DateField(blank=True, null=True)
