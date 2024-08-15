from django.urls import path

from . import views
urlpatterns = [
    path('employees/', views.EmployeesView.as_view(), name="employees"),
    path('positions/', views.PositionView.as_view(), name="positions"),
    path('projects/', views.ProjectView.as_view(), name="projects"),
    path('projects/<int:project_id>/delete/', views.ProjectView.as_view(), name="projects_delete"),
    path('projects/<int:project_id>/detail/', views.ProjectDetailView.as_view(), name="project_detail"),
    path('projects/<int:project_id>/<int:emp_id>/', views.ProjectDetailView.as_view(), name="project_action")
]