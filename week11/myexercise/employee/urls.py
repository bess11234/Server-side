from django.urls import path

from . import views
urlpatterns = [
    path("", views.EmployeeView.as_view(), name="employees"),
    path("employee/create/", views.EmployeeFormView.as_view(), name="employee_form"),
    path("project/", views.ProjectView.as_view(), name="projects"),
    path("project/create/", views.ProjectFormView.as_view(), name="project_form"),
    path('project/<int:project_id>/', views.ProjectDetailView.as_view(), name="project_detail"),
    path('project/<int:project_id>/kick/<int:employee_id>/', views.project_kick_staff, name="project_kickstaff"),
    path('project/<int:project_id>/delete/', views.project_delete, name="project_delete"),   
]