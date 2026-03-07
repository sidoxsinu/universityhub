from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('department/', views.department, name='department'),
    path('student_registration/', views.student_registration, name='student_registration'),
    path('registration_success/', views.registration_success, name='registration_success'),
]