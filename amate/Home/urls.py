from django.urls import path
from Home.views import Detail_Publication, Publications_list

urlpatterns =[
    path('', Publications_list.as_view(), name = 'home'),
    path('detail-publication/<int:pk>/', Detail_Publication.as_view(), name = 'detail_publication'),
]