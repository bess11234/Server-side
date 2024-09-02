from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
from .models import *
from .forms import EmployeeForm
# Create your views here.

class EmployeeView(View):

    def get(self, request):
        return render(request, "employee.html", {
            'employees' : Employee.objects.all()
        })

class EmployeeFormView(View):
    def get(self, request):
        form = EmployeeForm()
        return render(request, "employee_form.html",{
            'form': form
        })
    
    def post(self, request):
        form = EmployeeForm(request.POST)
        if (form.is_valid()):
            # first_name = form.cleaned_data["first_name"]
            # last_name = form.cleaned_data["last_name"]
            # gender = form.cleaned_data["gender"]
            # birth_date = form.cleaned_data["birth_date"]
            # hire_date = form.cleaned_data["hire_date"]
            # salary = form.cleaned_data["salary"]
            # position = form.cleaned_data["position"]
            Employee.objects.create(**form.cleaned_data)
            
            return redirect("employee")
        else:
            return render(request, "employee_form", {"form": form})

class PositionView(View):
    def get(self, request):
        return render(request, "position.html", {
            "positions": Position.objects.all()
        })
        
class ProjectView(View):
    def get(self, request):
        return render(request, "project.html", {
            "projects": Project.objects.all()
        })
    def delete(self, request, project_id):
        Project.objects.get(pk=project_id).delete()
        return JsonResponse({"status": 0})

class ProjectDetail(View):
    def get(self, request, project_id):
        return render(request, "project_detail.html", {
            "project": Project.objects.get(id=project_id)
        })
    def put(self, request, project_id, employee_id):
        Project.objects.get(pk=project_id).staff.add(employee_id)
        return JsonResponse({'status':0})
    def delete(self, request, project_id, employee_id):
        Project.objects.get(pk=project_id).staff.remove(employee_id)
        return JsonResponse({'status':0})