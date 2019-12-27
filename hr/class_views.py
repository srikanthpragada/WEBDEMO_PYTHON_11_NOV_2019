from django.views.generic import ListView
from .models import Employee


class EmployeesList(ListView):
    model = Employee
