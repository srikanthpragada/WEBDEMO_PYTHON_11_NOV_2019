from django.contrib import admin
from django.urls import path
from . import views, job_views, employee_views, class_views
from .rest import rest_views

urlpatterns = [
    path('index/', views.index),
    path("countries/", views.list_countries),
    path("country_info/", views.country_info),
    path("jobs/", job_views.list_jobs),
    path("addjob/", job_views.add_job),
    path("addjob2/", job_views.add_job2),
    path("emp/home/", employee_views.employee_home),
    path("emp/list/", employee_views.employee_list),
    path("emp/add/", employee_views.employee_add),
    path("emp/delete/<int:id>", employee_views.employee_delete),
    path("emp/edit/<int:id>", employee_views.employee_edit),
    path("emp/search/", employee_views.employee_search),
    path("emp/dosearch/", employee_views.search_employees),
    path("ajax/", views.ajax_demo),
    path("datetime/", views.ajax_datetime),
    path('employees/', class_views.EmployeesList.as_view()),  # class based view
    # Rest urls
    path('rest/employees/', rest_views.process_employees),
    path('rest/employees/<int:id>', rest_views.process_employee),
]
