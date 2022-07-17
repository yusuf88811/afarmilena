from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from marshmallow import ValidationError


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

    def validate_length(value, length=9):
        if value.isdigit():
            if len(str(value)) != length:
                raise ValidationError({'error': f"Имя пользователя должно быть равно символам {value}"})
        else:
            raise ValidationError({'error': f"просто введите номер телефона {value}"})

    # username = models.CharField(max_length=30, unique=False)
    phone = models.CharField(max_length=9, validators=[validate_length], unique=True)
    cite = models.CharField(max_length=50, choices=CITE)
    wedding_date = models.DateField(blank=True, null=True)
    # USERNAME_FIELD = 'phone'

    class Meta:
        ordering = ['-date_joined']
        verbose_name_plural = "Пользователи"

    def save(self, *args, **kwargs):
        super(CustomUser, self).save(*args, **kwargs)


class BlockList(models.Model):
    reason = models.CharField(max_length=250, blank=False, null=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

