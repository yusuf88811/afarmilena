from statistics import mode

from django.db import models


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).delete(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class SystemInformation(SingletonModel):
    name = models.CharField(max_length=250, blank=False, null=False)
    type = models.CharField(max_length=250, blank=False, null=False)
    description = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        super(SystemInformation, self).save(*args, **kwargs)


class SysteminfoImage(models.Model):
    system_info = models.ForeignKey(SystemInformation, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='', blank=True)
