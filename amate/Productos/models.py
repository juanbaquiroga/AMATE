from email.mime import image
from statistics import mode
from unicodedata import category
from django.db import models

# Create your models here.

class categoria(models.Model):
    name = models.CharField(max_length=15)
    description = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

class producto(models.Model):
    name = models.CharField(max_length=40)
    imagen = models.ImageField(upload_to='productos')
    price = models.FloatField()
    description = models.CharField(max_length=200, blank=True, null=True)
    category = models.ForeignKey(categoria,  on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'

