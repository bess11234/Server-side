from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *

from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.decorators import permission_classes
from .permissions import AppointmentsPermission
from rest_framework.authentication import TokenAuthentication

from django.utils.decorators import method_decorator

# Create your views here.
class DoctorList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        print(serializer.data, doctors)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class PatientList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AppointmentList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly, AppointmentsPermission]

    def get(self, request):
        appoints = Appointment.objects.all()
        serializer = AppointmentSerializer(appoints, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        request.data['created_by'] = request.user.id
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AppointmentElement(APIView):
    permission_classes = [IsAuthenticated, AppointmentsPermission]
    
    def get_object(self, pk):
        appoints = get_object_or_404(Appointment, pk=pk)
        self.check_object_permissions(self.request, appoints)
        return appoints

    def get(self, request, pk):
        appoints = self.get_object(pk)
        serializer = AppointmentSerializer(appoints)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        appoints = self.get_object(pk)
        self.check_object_permissions(request, appoints)
        request.data['created_by'] = request.user.id
        serializer = AppointmentSerializer(appoints, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        appoints = self.get_object(pk)
        self.check_object_permissions(request, appoints)
        serializer = AppointmentSerializer(appoints, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        appoints = self.get_object(pk)
        self.check_object_permissions(request, appoints)
        appoints.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)