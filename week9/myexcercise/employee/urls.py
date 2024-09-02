from django.urls import path
from .views import *
urlpatterns = [
    path("", EmployeeView.as_view(), name="employee"),
    path("employeeForm/", EmployeeFormView.as_view(), name="employee_form"),
]