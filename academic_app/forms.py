from django import forms
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


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control'}),
        help_text="Password must be at least 8 characters and contain letters and numbers."
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control'})
    )