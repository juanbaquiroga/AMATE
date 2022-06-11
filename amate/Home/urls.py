from django.urls import path
from Home.views import Detail_publication, List_publications, Create_publication, Delete_publication, Update_publication

urlpatterns =[
    path('', List_publications.as_view(), name = 'list_publications'),
    path('detail-publication/<int:pk>/', Detail_publication.as_view(), name = 'detail_publication'),
    path('create-publication/', Create_publication.as_view(), name = 'create_publication'),
    path('delete-publication/<int:pk>/', Delete_publication.as_view(), name = 'delete_publication'),
    path('update-publication/<int:pk>/', Update_publication.as_view(), name = 'update_publication'),
]