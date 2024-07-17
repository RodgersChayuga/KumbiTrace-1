from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="List All Records"),
    path('new', views.new, name="Create New Report"),
    path('view', views.view, name="View Entry"),
    path('verify', views.verify, name="Verify Report"),
    path('update', views.update, name="Update Entry"),
    path('self', views.self, name="Self Reporting"),
    path('arrest', views.abduction, name="Report Abduction")
]
