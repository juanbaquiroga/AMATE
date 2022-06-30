from django.urls import path
from Productos.views import list_products, Create_product, Detail_product, Delete_product, Update_product, search_product

urlpatterns =[
    path('', list_products, name = 'List_products'),
    path('create-product/', Create_product.as_view(), name = 'Create_product'),
    path('search-product/', search_product, name = 'search_products'),
    path('detail-product/<int:pk>/', Detail_product.as_view(), name = 'detail_product'),
    path('delete-product/<int:pk>/', Delete_product.as_view(), name = 'delete_product'),
    path('update-product/<int:pk>/', Update_product.as_view(), name = 'update_product'),
]