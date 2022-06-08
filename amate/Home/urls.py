from django.urls import path

from Home.views import Publications_list

urlpatterns =[
    path('', Publications_list.as_view(), name = 'home'),
]