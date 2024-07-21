from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Index Man!")


def view(request, record_id):
    return HttpResponse("verify %s", record_id)


def process(request, record_id):
    return HttpResponse("tester tester process %s", record_id)
