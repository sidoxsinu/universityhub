from django.shortcuts import render, redirect
from .models import Department, Student
from .forms import StudentRegistrationForm

def home(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'contact.html')

def department(request):
    return render(request, 'department.html', {
        "departments": Department.objects.all()
    })

def registration_success(request):
    return render(request, 'registration_success.html')

def student_registration(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_success')
    else:
        form = StudentRegistrationForm()
    departments = Department.objects.all()
    return render(request, 'student_registration.html', {'form': form, 'departments': departments})