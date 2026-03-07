from django.forms import ModelForm, TextInput, EmailInput, Select
from .models import Student

class StudentRegistrationForm(ModelForm):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'email', 'department')
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'department': Select(attrs={'class': 'form-control'}),
        }
