from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .models import *


def homepage(request):
    return render(request, 'kumbitraceweb/index.html')

def about(request):
    return render(request, 'kumbitraceweb/about.html')

def report(request):
    return render(request, 'kumbitraceweb/report.html')

def search(request):
    return render(request, 'kumbitraceweb/search.html')

def tip(request):
    return render(request, 'kumbitraceweb/tip.html')

def found(request):
    return render(request, 'kumbitraceweb/found.html')

def contact(request):
    return render(request, 'kumbitraceweb/contact.html')

def policy(request):
    return render(request, 'kumbitraceweb/data-protection-policy.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('logincustom'))  # Redirect to login page after successful registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'kumbitraceweb/register.html', {'form': form})

def logincustom(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome, {username}! You have been logged in.")
                return redirect('dashboard')
            else:
                print(f"Authentication failed for username: {username}")  # Debug print
                messages.error(request, "Invalid username or password.")
        else:
            print(f"Form errors: {form.errors}")  # Debug print
            messages.error(request, "Invalid username or password.")
    else:
        form = CustomAuthenticationForm()
    return render(request, 'kumbitraceweb/login.html', {'form': form})

@login_required(login_url=reverse_lazy('logincustom'))
def dashboard(request):
    return render(request, 'kumbitraceweb/dashboard.html')

def user_logout(request):
    logout(request)
    return redirect('homepage')  # Redirect to homepage after logout