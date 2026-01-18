from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from auth_app.models import *
from .forms import *



# Create your views here.
def register(request):
    if request.method=="POST":
        full_name=request.POST.get('full_name')
        username=request.POST.get('username')
        usertype=request.POST.get('usertype')
        password=request.POST.get('password')
        con_password=request.POST.get('con_password')
        email=request.POST.get('email')
        
        ex_username=UserModel.objects.filter(username=username).exists()
        if ex_username:
            print('this name has already exists')
            return redirect('register')
        if password == con_password:
            UserModel.objects.create_user(
                full_name=full_name,
                username=username,
                usertype=usertype,
                password=password,
                email=email
                )
            messages.success(request, "Register succesfully")
            return redirect('login')
    return render(request, 'auth/register.html')

def login_page(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=authenticate(request, username=username, password=password)
        
        if user:
            login(request, user)
            messages.success(request, "Login successfully")
            return redirect('homePage')
    return render(request, 'auth/login.html')


@ login_required
def homePage(request):
    
    return render(request, 'home.html')


@ login_required
def logoutpage(request):
    logout(request)
    return redirect('login')

#------Department--------

def departmentPage(request):
    dep_data=DepartmentModel.objects.all()
    context={
        'dep_data':dep_data
    }
    return render(request, 'department/departmentlist.html', context)


def addDepartment(request):
    if request.method=="POST":
        dep_form=DepartmentForm(request.POST)
        if dep_form.is_valid():
            dep_form.save()
            return redirect('departmentPage')
            
    dep_form=DepartmentForm()
    context={
        'dep_form':dep_form
    }
    return render(request, 'templetes/department/departadd.html', context)

def edite_department(request, id):
    department=DepartmentModel.objects.get(id=id)
    if request.method=="POST":
        dep_form=DepartmentForm(request.POST, instance=department)
        if dep_form.is_valid():
            dep_form.save()
            return redirect('departmentPage')
        
    dep_form=DepartmentForm(instance=department)
    context={
        'dep_form':dep_form
    }
    return render(request, 'templetes/department/edit_page.html', context)

def delete_department(request, id):
    department=DepartmentModel.objects.get(id=id)
    department.delete()
    return redirect('departmentPage')

#-------doctor-----

def doctor_list(request):
    dr_data=DoctorModel.objects.all()
    context={
        'dr_data':dr_data
    }
 
    return render(request, 'doctor/drlist.html', context)


def doctor_page(request):
    if request.method == "POST":
        form_dr=DoctorForm(request.POST)
        if form_dr.is_valid():
            form_dr.save()
            return redirect('doctor_list')
    form_dr=DoctorForm()
    context={
        'form_dr':form_dr
    }
        
    return render(request, 'templetes/doctor/dradd.html', context)

def edit_page(request,id):
    doctor=DoctorModel.objects.get(id = id)
    if request.method=="POST":
        form_dr=DoctorForm(request.POST, instance=doctor)
        if form_dr.is_valid():
           form_dr.save()
           return redirect('doctor_list')
       
       
    form_dr=DoctorForm(instance=doctor)
    context={
        'form_dr':form_dr
    }
    
    return render(request,'doctor/edit_dr.html', context)

def delete_page(request,id):
    doctor=DoctorModel.objects.get(id=id)
    doctor.delete()
    return redirect('doctor_list')
    
    
#--------Patient--------

def patient_list(request):
    patient_data=PatientModel.objects.all()
    context={
        'patient_data':patient_data
    }
    return render(request, 'patient/listpatient.html',context )

def add_patient(request):
    if request.method=="POST":
        patient_form=PatientForm(request.POST)
        if patient_form.is_valid():
            patient_form.save()
            return redirect('patient_list')
        
    patient_form=PatientForm()
    context={
        'patient_form':patient_form
    }
    return render(request, 'templetes/patient/addpatient.html', context)
    
    
def edite_patient(request, id):
    data=PatientModel.objects.get(id=id)
    if request.method=="POST":
        form_data=PatientForm(request.POST, instance=data)
        if form_data.is_valid():
            form_data.save()
            return redirect('patient_list')
        
    form_data=PatientForm(instance=data)
    context={
        'form_data':form_data
    }
    return render(request, 'templetes/patient/edit_patien.html', context)


def delete_patient(request, id):
    form_data=PatientModel.objects.get(id=id)
    form_data.delete()
    return redirect('patient_list')
    