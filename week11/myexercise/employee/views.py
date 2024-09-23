from django.shortcuts import render, redirect

from django.views import View

from .models import *
from .forms import *
from company.models import Position
from django.db import transaction
# Create your views here.

class EmployeeView(View):
    def get(self, request):
        employees =  Employee.objects.all()

        for i in employees:
            i.position = Position.objects.get(pk=i.position_id)

        return render(request, "employee.html", {
            "employees": employees
        })

class EmployeeFormView(View):
    def get(self, request):
        form = EmployeeForm()
        
        return render(request, "employee_form.html", {
            "form": form
        })
    
    @transaction.atomic
    def post(self, request):
        form = EmployeeForm(request.POST)
        
        if form.is_valid():
            location = form.cleaned_data.get("location")
            district = form.cleaned_data.get("district")
            province = form.cleaned_data.get("province")
            postal_code = form.cleaned_data.get("postal_code")

            # เพิ่มข้อมูล Employee
            employee = form.save()
            
            # เพิ่มข้อมูล Employee Address
            location = EmployeeAddress(location=location, employee=employee, 
                                       district=district, province=province,
                                       postal_code=postal_code)
            location.save()

            return redirect("employees")
        return render(request, "employee_form.html", {
            "form": form
        })
        
class ProjectView(View):
    def get(self, request):
        return render(request, "project.html", {
            "projects": Project.objects.all()
        })

class ProjectFormView(View):
    def get(self, request):
        form = ProjectForm()
        
        return render(request, "project_form.html", {
            "form": form
        })
        
    def post(self, request):
        form = ProjectForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("projects")
        return render(request, "project_form.html", {
            "form": form
        })

class ProjectDetailView(View):
    def get(self, request, project_id):
        project = Project.objects.get(id=project_id)
        form = ProjectForm(instance=project)
        
        staff = project.staff.all()
        for i in staff:
            i.position = Position.objects.get(pk=i.position_id)

        return render(request, "project_detail.html", {
            "form": form,
            "staff": staff,
            "id": project_id
        })
    
    def post(self, request, project_id):
        project = Project.objects.get(pk=project_id)
        form = ProjectForm(request.POST, instance=project)

        if form.is_valid():
            form.save()
            return redirect("projects")
        else:
            staff = project.staff.all()
            for i in staff:
                i.position = Position.objects.get(pk=i.position_id)
        return render(request, "project_detail.html", {
            "form": form,
            "staff": staff,
            "id": project_id
        })
def project_kick_staff(request, project_id, employee_id):
    Project.objects.get(pk=project_id).staff.remove(employee_id)
    return redirect("project_detail", project_id)

def project_delete(request, project_id):
    Project.objects.get(id=project_id).delete()
    return redirect("projects")