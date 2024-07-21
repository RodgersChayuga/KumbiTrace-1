from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.homepage, name=""),

    path('about-us', views.about, name="about"),

    path('search', views.search, name="search"),

    path('tip', views.tip, name="tip"),

    path('found', views.found, name="found"),

    path('contact-us', views.contact, name="contact"),

    path('privacy-policy', views.policy, name="policy"),

    path('register', views.register, name="register"),

    path('login', views.logincustom, name="logincustom"),

    path('dashboard', views.dashboard, name="dashboard"),

    path('report', views.report_missing_person, name='report_missing_person'),

    path('missing_person/<int:case_number>/', views.missing_person_detail, name='missing_person_detail'),

    path('user-logout', views.user_logout, name="user-logout"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)