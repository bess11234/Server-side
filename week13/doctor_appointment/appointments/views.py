from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *

# Create your views here.
class DoctorList(APIView):
    def get(self, request):
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        print(serializer.data, doctors)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class PatientList(APIView):
    def get(self, request):
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AppointmentList(APIView):
    def get(self, request):
        appoints = Appointment.objects.all()
        serializer = AppointmentSerializer(appoints, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AppointmentElement(APIView):
    def get_object(self, pk):
        appoints = get_object_or_404(Appointment, pk=pk)
        return appoints

    def get(self, request, pk):
        appoints = self.get_object(pk)
        serializer = AppointmentSerializer(appoints)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        appoints = self.get_object(pk)
        serializer = AppointmentSerializer(appoints, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        appoints = self.get_object(pk)
        appoints.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)