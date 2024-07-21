from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# Create your views here
from .models import *


# Create your views here.
def index(request):
    return HttpResponse("Home Page: Record")


def new(request):
    return HttpResponse("Create New record")


def view(request, record_id):
    return HttpResponse("View %s", record_id)


def verify(request, record_id):
    return HttpResponse("Verify %s", record_id)


def update(request, record_id):
    return HttpResponse("Updated %s", record_id)


def self(request, record_id):
    return HttpResponse("Updated %s", record_id)


def abduction(request, record_id):
    return HttpResponse("Updated %s", record_id)
