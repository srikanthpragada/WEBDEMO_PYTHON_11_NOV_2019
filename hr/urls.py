from django.contrib import admin
from django.urls import path
from . import views, job_views

urlpatterns = [
    path('index/', views.index),
    path("countries/", views.list_countries),
    path("country_info/", views.country_info),
    path("jobs/", job_views.list_jobs),
    path("addjob/", job_views.add_job),
]
