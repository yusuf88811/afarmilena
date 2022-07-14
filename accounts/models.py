from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class CustomUser(AbstractUser):
    TOSHKENT = "Toshkent"
    TOSHKENT_V = "Toshkent_v"
    ANDIJON = "Andijon "
    BUXORO = "Buxoro"
    FARGONA = "Farg'ona"
    SIRDARYO = "Sirdaryo"
    JIZZAX = "Jizzax"
    NAMANGAN = "Namangan"
    NAVOIY = "Navoiy"
    QORAQAL = "Qoraqalpog'iston Respublikasi"
    SAMARQAND = "Samarqand"
    SURXONDARYO = "Surxondaryo"
    XORAZM = "Xorazm"
    QASHQADARYO = "Qashqadaryo"

    CITE = (
        (TOSHKENT, "Toshkent"),
        (TOSHKENT_V, "Toshkent_v"),
        (ANDIJON, "Andijon"),
        (BUXORO, "Buxoro"),
        (FARGONA, "Farg'ona"),
        (SIRDARYO, "Sirdaryo"),
        (JIZZAX, "Jizzax"),
        (NAMANGAN, "Namangan"),
        (NAVOIY, "Navoiy"),
        (QORAQAL, "Qoraqalpog'iston Respublikasi"),
        (SAMARQAND, "Samarqand"),
        (SURXONDARYO, "Surxondaryo"),
        (XORAZM, "Xorazm"),
        (QASHQADARYO, "Qashqadaryo"),

    )

    phone = models.CharField(max_length=13, null=False, blank=True, unique=True)
    cite = models.CharField(max_length=50, choices=CITE)
    wedding_date = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ['-date_joined']

    def save(self, *args, **kwargs):
        super(CustomUser, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Пользователи"
