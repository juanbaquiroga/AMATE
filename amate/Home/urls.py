from django.urls import path

from Home.views import Publications_list, Detail_Publication, Create_Publication, Delete_Publication, Update_Publication, about_us

urlpatterns =[
    path('', Publications_list.as_view(), name = 'home'),
    path('about-us/', about_us, name = 'about-us'),
    path('detail-publication/<int:pk>/', Detail_Publication.as_view(), name = 'detail-publication'),
    path('delete-publication/<int:pk>/', Delete_Publication.as_view(), name = 'delete-publication'),
    path('update-publication/<int:pk>/', Update_Publication.as_view(), name = 'update-publication'),
    path('create-publication/', Create_Publication.as_view(), name = 'create-publication'),
]