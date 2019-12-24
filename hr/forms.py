import django.forms as forms
from django.forms import ModelForm
from .models import Employee


class JobForm(forms.Form):
    title = forms.CharField(max_length=30)
    location = forms.CharField(max_length=20, required=False)
    minsal = forms.IntegerField(min_value=5000, required=False)


class UpdateJobForm(forms.Form):
    id = forms.IntegerField()
    minsal = forms.IntegerField(min_value=5000, required=False)


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
