from django.shortcuts import render

from django.views import View
from .models import *

from django.http import HttpResponse, JsonResponse

# Create your views here.

class EmployeesView(View):
    def get(self, request):
        return render(request, 'employee.html', {
            "employees": Employee.objects.all()
        })

class PositionView(View):
    def get(self, request):
        return render(request, 'position.html', {
            "positions" : Position.objects.all()
        })

class ProjectView(View):
    def get(self, request):
        return render(request, 'project.html', {
            "projects": Project.objects.all()
        })
    
    def delete(self, request, project_id):
        if (Project.objects.get(pk=project_id).delete()):
            return HttpResponse("\"{'status':'0'}\"")
        return HttpResponse("\"{'status':'1'}\"")

class ProjectDetailView(View):
    def get(self, request, project_id):
        return render(request, 'project_detail.html',{
            "project": Project.objects.get(id=project_id)
        })
    
    def put(self, request, project_id, emp_id):
        project = Project.objects.get(pk=project_id)
        project.staff.add(emp_id)
        return HttpResponse("\"{'status':'0'}\"")

    def delete(self, request, project_id, emp_id):
        project = Project.objects.get(pk=project_id)
        project.staff.remove(emp_id)
        return JsonResponse({'status': 0}, status=200)