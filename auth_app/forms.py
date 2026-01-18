from django import forms
from .models import *


class DepartmentForm(forms.ModelForm):
    class Meta:
        model=DepartmentModel
        fields='__all__'
        
        
class DoctorForm(forms.ModelForm):
    class Meta:
        model=DoctorModel
        fields='__all__'
        
        
class PatientForm(forms.ModelForm):
    class Meta:
        model=PatientModel
        fields='__all__'
        

class AppointmentForm(forms.ModelForm):
    class Meta:
        model=AppointmentModel
        fields='__all__'