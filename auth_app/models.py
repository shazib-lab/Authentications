from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class UserModel(AbstractUser):
    
    USER_TYPE=[
        ('Admin', 'Admin'),
        ('User', 'User'),
    ]
    full_name=models.CharField(max_length=100, null=True)
    usertype=models.CharField(choices=USER_TYPE, max_length=100, null=True)
    
    def __str__(self):
        return self.full_name
    
class DepartmentModel(models.Model):
    name=models.CharField(max_length=100, null=True)
    location=models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return f"{self.name}"
    
class DoctorModel(models.Model):
    name=models.CharField(max_length=100, null=True)
    SPECIALIZATION=[
        ('Cardiologists', 'Cardiologists'),
        ('Neurologists ', 'Neurologists '),
        ('Dermatologists ', 'Dermatologists '),
        ('Gastroenterologists', 'Gastroenterologists'),
        ('Oncologists', 'Oncologists'),
    ]
    specilization=models.CharField(choices=SPECIALIZATION, max_length=100, null=True)
    phone=models.CharField(max_length=20, null=True)
    email=models.EmailField(null=True)
    department=models.ForeignKey(DepartmentModel, on_delete=models.CASCADE, related_name='department_name', max_length=100, null=True)
    
    def __str__(self):
        return f"{self.name}"
    
class PatientModel(models.Model):
    name=models.CharField(max_length=100, null=True)
    age=models.IntegerField(null=True)
    GENDER=[
        ('Male', 'Male'),
        ('Female', 'Femal')
    ]
    gender=models.CharField(choices=GENDER, max_length=100, null=True)
    phone=models.CharField(max_length=20, null=True)
    address=models.TextField(null=True)
    doctor=models.ForeignKey(DoctorModel, on_delete=models.CASCADE, related_name='doctor_name', max_length=100, null=True)
    
    def __str__(self):
        return f"{self.name}"
    
    
class AppointmentModel(models.Model):
    patient=models.ForeignKey(PatientModel, on_delete=models.CASCADE, related_name='patirent_name', max_length=100, null=True)
    doctor=models.ForeignKey(DoctorModel, on_delete=models.CASCADE, related_name='doctors_name', max_length=100, null=True)
    STATUS=[
        ('Pending', 'Pending'),
        (' Completed', ' Completed'),
        ('Cancelled', 'Cancelled'),
    ]
    status=models.CharField(choices=STATUS, max_length=100, null=True)
    
    def __str__(self):
        return f"{self.patient.naem}"