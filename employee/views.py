from django.shortcuts import render

# Create your views here.
from employee.models import Employee
employees= Employee.object.all()
print(employees)