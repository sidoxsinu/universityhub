from django.urls import path
from . import views
from django.contrib.auth import views as auth_views   # ← ADD THIS

urlpatterns = [
    path('', views.home, name='home'),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # ← ADD THIS

    path('contact/', views.contact, name='contact'),
    path('department/', views.department, name='department'),
    path('student_registration/', views.student_registration, name='student_registration'),
    path('registration_success/', views.registration_success, name='registration_success'),
]