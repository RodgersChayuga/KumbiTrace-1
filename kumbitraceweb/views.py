from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import MissingPersonForm, TipForm
from .models import MissingPerson, Tip
from .forms import CustomUserCreationForm, CustomAuthenticationForm, MissingPersonForm, TipForm
from .models import *
from django.utils import timezone
import pytz

def homepage(request):
    return render(request, 'kumbitraceweb/index.html')

def about(request):
    return render(request, 'kumbitraceweb/about.html')

@login_required(login_url=reverse_lazy('logincustom'))
def report_missing_person(request):
    if request.method == 'POST':
        form = MissingPersonForm(request.POST, request.FILES)
        if form.is_valid():
            missing_person = form.save(commit=False)
            missing_person.reporter = request.user
            
            # Handle file upload
            if 'photo' in request.FILES:
                missing_person.photo = request.FILES['photo']
            
            missing_person.save()
            messages.success(request, f'Missing person report submitted successfully. Case Number: {missing_person.case_number}')
            return redirect('dashboard')
        else:
            messages.error(request, 'There was an error in your form. Please correct it and try again.')
    else:
        form = MissingPersonForm()
    
    return render(request, 'kumbitraceweb/report_missing_person.html', {'form': form})

def search(request):
    query = request.GET.get('query')
    missing_persons = None
    if query:
        missing_persons = MissingPerson.objects.filter(
            models.Q(name__icontains=query) |
            models.Q(case_number__icontains=query)
        )
    return render(request, 'kumbitraceweb/search.html', {'missing_persons': missing_persons, 'query': query})

def tip(request):
    if request.method == 'POST':
        form = TipForm(request.POST)
        if form.is_valid():
            tip = form.save(commit=False)
            tip.ip_address = request.META.get('REMOTE_ADDR')
            if request.user.is_authenticated:
                tip.submitted_by = request.user
            else:
                tip.is_anonymous = True
            tip.save()
            messages.success(request, 'Tip submitted successfully.')
            return redirect('homepage')
    else:
        form = TipForm()
    return render(request, 'kumbitraceweb/tip.html', {'form': form})

def found(request):
    found_persons = MissingPerson.objects.filter(status='found')
    return render(request, 'kumbitraceweb/found.html', {'found_persons': found_persons})

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
    user_reports = MissingPerson.objects.filter(reporter=request.user).order_by('-date_reported')
    return render(request, 'kumbitraceweb/dashboard.html', {'user_reports': user_reports})

def user_logout(request):
    auth.logout(request)
    return render(request, 'kumbitraceweb/index.html')

def missing_person_detail(request, case_number):
    missing_person = get_object_or_404(MissingPerson, case_number=case_number)
    tips = missing_person.tips.all().order_by('-date_submitted')
    
    if request.method == 'POST':
        tip_form = TipForm(request.POST)
        if tip_form.is_valid():
            tip = tip_form.save(commit=False)
            tip.missing_person = missing_person
            tip.ip_address = request.META.get('REMOTE_ADDR')
            if request.user.is_authenticated:
                tip.submitted_by = request.user
            else:
                tip.is_anonymous = True
            tip.save()
            messages.success(request, 'Tip submitted successfully.')
            return redirect('missing_person_detail', case_number=case_number)
        else:
            messages.error(request, 'There was an error in your tip. Please correct it and try again.')
    else:
        tip_form = TipForm(initial={'missing_person': missing_person})
    
    return render(request, 'kumbitraceweb/missing_person_detail.html', {
        'missing_person': missing_person,
        'tip_form': tip_form,
        'tips': tips
    })