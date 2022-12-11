from django.db import models


# Create your models here.
class Proyecto(models.Model):
    foto = models.CharField(max_length=250, blank=False)
    titulo = models.CharField(max_length=150, blank=False)
    descripcion = models.CharField(max_length=200, blank=False)
    tags = models.CharField(max_length=80, blank=False)
    url_github = models.CharField(max_length=250, blank=False)

    def save(self, *args, **kwargs):
        return super(Proyecto, self).save(*args, **kwargs)

