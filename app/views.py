from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from . import views
from .models import Product
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products':Product})


            
            


def logout_user(request):
    pass

