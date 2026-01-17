from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *



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