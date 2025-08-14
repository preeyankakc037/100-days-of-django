from django.http import HttpResponse
from employee.models import Employee 
from employee.models import Employee

def home(request):
    
    employees= Employee.object.all()    
    print(employees)
    return HttpResponse('<h3> Hello World </h3> ')