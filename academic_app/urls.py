from django.urls import path
from . import views
from django.contrib.auth import views as auth_views   # ← ADD THIS

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='first_page.html'), name='first_page'),  # ← ADD THIS
    path('home/', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # ← ADD THIS
    path('contact/', views.contact, name='contact'),
    path('department/', views.department, name='department'),
    path('student_registration/', views.student_registration, name='student_registration'),
    path('registration_success/', views.registration_success, name='registration_success'),
    path('register/', views.register, name='register'),
   path(
    'logout/',
    auth_views.LogoutView.as_view(template_name='logout.html'),
    name='logout'
) ]