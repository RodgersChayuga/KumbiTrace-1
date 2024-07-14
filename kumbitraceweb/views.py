from decimal import Decimal
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.urls import reverse_lazy

#Create your views here
from .models import *


def homepage(request):
    return render(request, 'kumbitraceweb/index.html')

def about(request):
    return render(request, 'kumbitraceweb/about.html')

def report(request):
    return render(request, 'kumbitraceweb/report.html')

def search(request):
    return render(request, 'kumbitraceweb/search.html')

def contact(request):
    return render(request, 'kumbitraceweb/contact.html')

def policy(request):
    return render(request, 'kumbitraceweb/data-protection-policy.html')

def register(request):
    return render(request, 'kumbitraceweb/register.html')

def login(request):
    return render(request, 'kumbitraceweb/login.html')

def user_logout(request):
    auth.logout(request)
    return render(request, 'kumbitraceweb/index.html')