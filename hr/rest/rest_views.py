from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from hr.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'name', 'desg', 'salary')


@api_view(['GET', 'POST'])
def process_employees(request):
    if request.method == "GET":
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)
    else:  # Post
        employee = EmployeeSerializer(data=request.data)
        if employee.is_valid():
            employee.save()  # insert into table
            return Response(employee.data)
        else:
            return Response(employee.errors, status=400)  # bad request


@api_view(['GET', 'DELETE'])
def process_employee(request, id):
    try:
        employee = Employee.objects.get(id=id)
    except:
        return Response(status=404)  # not found

    if request.method == "GET":
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
    else:  # DELETE
        employee.delete()
        return Response(status=204)  # No data
