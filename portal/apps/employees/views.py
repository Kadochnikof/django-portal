from django.shortcuts import render
from django.http import Http404
from .models import Employee
# Create your views here.


def employees(request):
    all_employees = Employee.objects.order_by('-employee_fullname')
    return render(request, 'employees/list.html', {'employees': all_employees})


def detail(request, employee_id):
    try:
        employee = Employee.objects.get(id=employee_id)
    except Exception:
        raise Http404(
            'Ой, кажется, такой страницы нет :(')

    return render(request, 'employees/employee.html', {'employee': employee})
