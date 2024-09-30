from django.urls import path

from . import views
urlpatterns = [
    path("doctors/", views.DoctorList.as_view()),
    path("patients/", views.PatientList.as_view()),
    path("appointments/", views.AppointmentList.as_view()),
    path("appointments/<int:pk>/", views.AppointmentElement.as_view()),
]