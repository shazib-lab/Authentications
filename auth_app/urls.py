from .views import *
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', register, name="register"),
    path('login_page/', login_page, name="login"),
    path('homePage/', homePage, name="homePage"),
    path('logoutpage/', logoutpage, name="logout"),
    
    #-------Department------
    path('departmentPage/', departmentPage, name="departmentPage"),
    path('addDepartment/', addDepartment, name="addDepartment"),
    path('edite_department/<int:id>/', edite_department, name="edite_department"),
    path('delete_department/<int:id>/', delete_department, name="delete_department"),
    
    
    #-----doctor--------
    path('doctor_list/', doctor_list, name="doctor_list"),
    path('doctor_page/', doctor_page, name="doctor_page"),
    path('edit_page/<int:id>/', edit_page, name="edit_page"),
    path('delete_page/<int:id>/', delete_page, name="delete_page"),
    
    #------patient-------
    path('patient_list/', patient_list, name="patient_list"),
    path('add_patient/', add_patient, name="add_patient"),
    path('edite_patient/<int:id>/', edite_patient, name="edite_patient"),
    path('delete_patient/<int:id>/', delete_patient, name="delete_patient"),
    
]