from django import forms

from django.utils import timezone
from django.core.exceptions import ValidationError
from .models import *

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        widgets = {
            "birth_date": forms.DateInput(attrs={"type":"date"}),
            "hire_date": forms.DateInput(attrs={"type":"date"})
        }

    gender = forms.ChoiceField(
        choices=( ("", "---------"), ("M", "Male"), ("F", "Female"), ("LGBT", "LGBT") )
    )
    
    def clean_hire_date(self):
        hire_date = self.cleaned_data.get("hire_date")
        birth_date = self.cleaned_data.get("birth_date")
        if hire_date > timezone.now().date():
            raise ValidationError(
                "Cannot hired employee from future."
            )
        elif hire_date <= birth_date:
            raise ValidationError(
                "Cannot hired employee that yet not birth."
            )
        return hire_date

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            "name",
            "manager",
            "due_date",
            "start_date",
            "description",
            "staff"
        ]
        widgets = {
            "due_date": forms.DateInput(attrs={"type": "date"}),
            "start_date": forms.DateInput(attrs={"type": "date"}),
            # "staff": forms.CheckboxSelectMultiple(attrs={"style": "border: 0px"})
        }
    
    def clean_start_date(self):
        cleaned_data = super().clean()
        start_date = cleaned_data['start_date']
        due_date = cleaned_data['due_date']
        if start_date >= due_date:
            self.add_error("start_date", "Cannot start project when project finished.")
        return start_date