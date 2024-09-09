from django.shortcuts import render, redirect

from datetime import datetime, timedelta
from django.views import View
from django.utils import timezone
from django.db.models import Q

from bookings.models import *
from .forms import BookingForm
# Create your views here.

class BookingView(View):
    def get(self, request):
        query = request.GET
        
        bookings = Booking.objects.filter(start_time__gt=timezone.now()).order_by("start_time")
        
        if (query.get("search")):
            bookings = Booking.objects.filter(
                Q(room__name__icontains=query.get("search")) | Q(staff__name__icontains=query.get("search"))
            )

        return render(request, "booking-list.html", {
            "bookings": bookings
        })
        
class BookingCreate(View):
    
    def get(self, request):
        form = BookingForm()
        
        return render(request, "booking.html",{
            "form": form
        })
        
    def post(self, request):
        form = BookingForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("booking-list")
        else:
            return render(request, "booking.html",{
            "form": form
        })

class BookingDelete(View):
    def get(self, request, booking_id):
        Booking.objects.get(pk=booking_id).delete()
        return redirect("booking-list")