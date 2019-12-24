from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.db.models import Count, Avg
from .models import Employee
from django.core.exceptions import ObjectDoesNotExist
from .forms import EmployeeForm


def employee_home(request):
    summary = Employee.objects.all().aggregate(
        emp_count=Count('id'), avg_salary=Avg('salary'))

    return render(request, 'employee_home.html',
                  {'summary': summary})


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html',
                  {'employees': employees})



def employee_delete(request, id):
    try:
        emp = Employee.objects.get(id=id)
        emp.delete()
        return redirect("/hr/emp/list")
    except ObjectDoesNotExist:
        return render(request, 'employee_delete.html',
                      {'msg': 'Employee Id Not Found!'})
    except:
        return render(request, 'employee_delete.html',
                      {'msg': 'Author could not be deleted!'})


def employee_add(request):
    if request.method == "GET":
        form = EmployeeForm()
        return render(request, 'employee_add.html',
                      {'form': form})
    else:
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()  # Add employee to table
            return redirect("/hr/emp/list")
        else:
            return render(request, 'employee_add.html',
                          {'form': form})

#
def employee_edit(request, id):
    if request.method == "GET":
        try:
            emp = Employee.objects.get(id=id)
            form = EmployeeForm(instance=emp)
            return render(request, 'employee_edit.html',
                          {'form': form})
        except ObjectDoesNotExist:
            return render(request, 'employee_edit.html',
                          {'msg': 'Employee Id Not Found!'})
    else:  # POST
        emp  = Employee.objects.get(id=id)
        form = EmployeeForm(instance=emp, data=request.POST)
        form.save()   # Update employee in table
        return redirect("/hr/emp/list")

#
# def author_search(request):
#     return render(request, 'author_search.html')
#
#
# def author_do_search(request):
#     name = request.GET['name']
#     # convert author objects to dict
#     authors = list(Author.objects.filter(name__contains=name).values())
#     # send list of dict in the form of array of json objects
#     return JsonResponse(authors, safe=False)
