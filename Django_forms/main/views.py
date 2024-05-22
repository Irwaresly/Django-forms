from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmployeeForm


# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def employee_data(request):
    form = EmployeeForm()
    return render(request, 'main/employee.html', {'form': form})
