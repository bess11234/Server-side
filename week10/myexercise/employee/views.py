from django.shortcuts import render, redirect

from django.views import View

from .models import *
from .forms import *
# Create your views here.

class EmployeeView(View):
    def get(self, request):
        return render(request, "employee.html", {
            "employees": Employee.objects.all()
        })

class EmployeeFormView(View):
    def get(self, request):
        form = EmployeeForm()
        
        return render(request, "employee_form.html", {
            "form": form
        })
    
    def post(self, request):
        form = EmployeeForm(request.POST)
        
        if form.is_valid():
            form.save()
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
        
        return render(request, "project_detail.html", {
            "form": form,
            "staff": project.staff.all(),
            "id": project_id
        })
    
    def post(self, request, project_id):
        project = Project.objects.get(pk=project_id)
        form = ProjectForm(request.POST, instance=project)
        
        if form.is_valid():
            form.save()
            return redirect("projects")
        return render(request, "project_detail.html", {
            "form": form,
            "staff": project.staff.all(),
            "id": project_id
        })
def project_kick_staff(request, project_id, employee_id):
    Project.objects.get(pk=project_id).staff.remove(employee_id)
    return redirect("project_detail", project_id)

def project_delete(request, project_id):
    Project.objects.get(id=project_id).delete()
    return redirect("projects")