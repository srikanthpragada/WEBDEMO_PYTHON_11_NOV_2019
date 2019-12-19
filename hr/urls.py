from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path("countries/", views.list_countries),
    path("country_info/", views.country_info)
]
