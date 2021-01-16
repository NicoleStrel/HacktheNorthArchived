from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bucketlist/', views.bucketlist, name='bucketlist'),
    path('search/', views.search, name='search'),
]