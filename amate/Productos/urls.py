from django.urls import path
from Productos.views import list_products, Create_product, Detail_product, Delete_product, Update_product, search_product, List_category, Update_category, Delete_category, Create_category

urlpatterns =[
    path('', list_products, name = 'List_products'),
    path('create-product/', Create_product.as_view(), name = 'Create_product'),
    path('search-product/', search_product, name = 'search_products'),
    path('detail-product/<int:pk>/', Detail_product.as_view(), name = 'detail_product'),
    path('delete-product/<int:pk>/', Delete_product.as_view(), name = 'delete_product'),
    path('update-product/<int:pk>/', Update_product.as_view(), name = 'update_product'),
    path('list-category/', List_category.as_view(), name = 'List_category'),
    path('create-category/', Create_category.as_view(), name = 'Create_category'),
    path('delete-category/<int:pk>/', Delete_category.as_view(), name = 'delete_category'),
    path('update-category/<int:pk>/', Update_category.as_view(), name = 'update_category'),
]