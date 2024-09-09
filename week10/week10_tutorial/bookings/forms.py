from django import forms
from django.core.exceptions import ValidationError

from .models import Booking

class BookingForm(forms.ModelForm):
    start_time = forms.SplitDateTimeField(widget=forms.SplitDateTimeWidget(
        date_attrs={"class": "input", "type": "date"},
        time_attrs={"class": "input", "type": "time"},
    ))
    
    end_time = forms.SplitDateTimeField(widget=forms.SplitDateTimeWidget(
        date_attrs={"class": "input", "type": "date"},
        time_attrs={"class": "input", "type": "time"},
    ))
    
    class Meta:
        model = Booking
        fields = [
            "room",
            "staff",
            "email",
            "start_time",
            "end_time",
            "purpose"
        ]
        widgets = {
            "email": forms.TextInput(attrs={"class": "input"}),
            "purpose": forms.Textarea(attrs={"rows": 5, "class": "textarea"})
        }
    
    def clean(self):
        cleaned_data = super().clean()
        room = cleaned_data.get("room")
        start_time = cleaned_data.get("start_time")
        end_time = cleaned_data.get("end_time")
        
        if start_time and end_time and end_time < start_time:
            raise ValidationError(
                "End time cannot be before start time"
            )
        
        bookings = Booking.objects.filter(
            start_time__lte=end_time,
            end_time__gte = start_time,
            room=room
        )
        if bookings.count() > 0:
            raise ValidationError(
                "This room has already been booked for the selected time"
            )
        return cleaned_data
