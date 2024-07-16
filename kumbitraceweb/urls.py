from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.homepage, name=""),

    path('about-us', views.about, name="about"),

    path('report', views.report, name="report"),

    path('search', views.search, name="search"),

    path('tip', views.tip, name="tip"),

    path('found', views.found, name="found"),

    path('contact-us', views.contact, name="contact"),

    path('privacy-policy', views.policy, name="policy"),

    path('register', views.register, name="register"),

    path('login', views.logincustom, name="logincustom"),

    path('dashboard', views.dashboard, name="dashboard"),

    path('user-logout', views.user_logout, name="user-logout"),

]