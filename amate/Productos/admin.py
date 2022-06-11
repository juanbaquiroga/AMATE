from asyncio import gather
from unicodedata import category
from django.contrib import admin
from Productos.models import producto,  categoria

# Register your models here.


@admin.register(producto)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'active']

@admin.register(categoria)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']