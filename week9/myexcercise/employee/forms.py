from django import forms
from .models import Position

class EmployeeForm(forms.Form):
    M = "Male"
    F = "Female"
    LGBT = "LGBT"
    GENDER_CHOICES = (
        (1, M),
        (2, F),
        (3, LGBT)
    )
    first_name = forms.CharField(max_length=155)
    last_name = forms.CharField(max_length=155)
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.Select,
        initial=1
    )
    birth_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    hire_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    salary = forms.DecimalField(initial=0, max_digits=10, decimal_places=2)
    position = forms.ModelChoiceField(
        queryset=Position.objects.all(),
        to_field_name="id",
        required=False
    )