import django.forms as forms


class JobForm(forms.Form):
    title = forms.CharField(max_length=30)
    location = forms.CharField(max_length=20, required=False)
    minsal = forms.IntegerField(min_value=5000, required=False)


class UpdateJobForm(forms.Form):
    id  = forms.IntegerField()
    minsal = forms.IntegerField(min_value=5000, required=False)