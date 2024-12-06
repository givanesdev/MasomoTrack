from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Member,Course, Performance, Student



# Registration Form
class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'email', 'phone', 'role']


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description', 'teacher']

class PerformanceForm(forms.ModelForm):
    class Meta:
        model = Performance
        fields = ['student', 'course', 'grade', 'score']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['user', 'date_of_birth']

    date_of_birth = forms.DateField(input_formats=['%Y-%m-%d'])  # Keep date format


