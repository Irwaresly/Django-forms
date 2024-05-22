from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
      emp_name = forms.CharField()
      emp_salary = forms.IntegerField()