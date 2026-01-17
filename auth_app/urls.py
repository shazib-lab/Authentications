from .views import *
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', register, name="register"),
    path('login_page/', login_page, name="login"),
    path('homePage/', homePage, name="homePage"),
    path('logoutpage/', logoutpage, name="logout"),
    
]