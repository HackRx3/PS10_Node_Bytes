from django.contrib import admin
from django.urls import path
from Home import views 
urlpatterns = [
    path('', views.index,name='Home'),
    path("help", views.help,name='help'),
    path("about",views.about,name='about')
]
