from email.mime import image
from statistics import mode
from unicodedata import category
from django.db import models

# Create your models here.

class Publicacion(models.Model):
    title = models.CharField(max_length=15)
    text = models.CharField(max_length=400)
    imagen = models.ImageField(upload_to='home', null=True, blank= True)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Publicacion'
        verbose_name_plural = 'Publicaciones'