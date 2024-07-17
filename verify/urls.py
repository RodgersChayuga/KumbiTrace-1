from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Verification Dashboard"),
    path('view', views.view, name="View Record"),
    path('process', views.process, name="Process Record"),
]
