from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(UserModel)
admin.site.register(DepartmentModel)
admin.site.register(DoctorModel)
admin.site.register(PatientModel)