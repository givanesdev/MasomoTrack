from django.contrib.auth.models import User
from django.db.models import Avg
from django.shortcuts import render,redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from .forms import CustomLoginForm
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseForbidden
from .models import Member,Course, Performance, Student
from .forms import MemberForm, CourseForm, PerformanceForm, StudentForm  # Ensure you create a form for Student
from django.http import HttpResponseRedirect
from django.urls import reverse
import logging
logger = logging.getLogger(__name__)
from django.contrib.auth.decorators import login_required
from masomoapp.helpers import check_role



# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def courses(request):
    return render(request, 'courses.html')

def details(request):
    return render(request, 'course-details.html')

def starter(request):
    return render(request, 'starter-page.html')

def trainers(request):
    return render(request, 'trainers.html')

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user to the database
            login(request, user)  # Automatically log the user in after registration
            return redirect('index')  # Redirect to home page or another page
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        if User.objects.filter(
                username=request.POST['username'],
                password=request.POST['password']
        ).exists():
            return render(request, 'index.html')
        else:
            return render(request, 'login.html')

    else:
        return render(request, 'login.html')
def member_list(request):
    members = Member.objects.all()
    return render(request, 'members/member_list.html', {'members': members})

def member_detail(request, pk):
    member = get_object_or_404(Member, pk=pk)
    return render(request, 'members/member_detail.html', {'member': member})

def member_create(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberForm()
    return render(request, 'members/member_form.html', {'form': form})

def member_update(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberForm(instance=member)
    return render(request, 'members/member_form.html', {'form': form})

def member_delete(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        member.delete()
        return redirect('member_list')
    return render(request, 'members/member_confirm_delete.html', {'member': member})

# View to list all courses
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'masomoapp/course_list.html', {'courses': courses})


def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'masomoapp/course_form.html', {'form': form})

def course_update(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'masomoapp/course_form.html', {'form': form})

def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    return render(request, 'masomoapp/course_confirm_delete.html', {'course': course})


def performance_list(request):
    performances = Performance.objects.all()
    return render(request, 'masomoapp/performance_list.html', {'performances': performances})


def performance_create(request):
    if request.method == 'POST':
        form = PerformanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('performance_list')
    else:
        form = PerformanceForm()
    return render(request, 'masomoapp/performance_form.html', {'form': form})


def performance_update(request, pk):
    performance = get_object_or_404(Performance, pk=pk)
    if request.method == 'POST':
        form = PerformanceForm(request.POST, instance=performance)
        if form.is_valid():
            form.save()
            return redirect('performance_list')
    else:
        form = PerformanceForm(instance=performance)
    return render(request, 'masomoapp/performance_form.html', {'form': form})

def performance_delete(request, pk):
    performance = get_object_or_404(Performance, pk=pk)
    if request.method == 'POST':
        performance.delete()
        return redirect('performance_list')
    return render(request, 'masomoapp/performance_confirm_delete.html', {'performance': performance})

# List all students
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

# Add new student
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_create.html', {'form': form})


def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_create.html', {'form': form})



@login_required
def dashboard(request):
    if request.user.is_teacher or request.user.is_admin:
        # Fetch data based on user role
        if request.user.is_admin:
            total_courses = Course.objects.count()
            total_students = Student.objects.count()
        else:  # For teachers, show only their courses and students
            total_courses = Course.objects.filter(teacher=request.user).count()
            total_students = Student.objects.filter(courses__teacher=request.user).count()

        performances = Performance.objects.all()

        if performances.exists():
            average_performance = performances.aggregate(Avg('grade'))['grade__avg']
        else:
            average_performance = 0

        total_performances = performances.count()

        context = {
            'total_courses': total_courses,
            'total_students': total_students,
            'average_performance': average_performance,
            'total_performances': total_performances,
        }

        return render(request, 'dashboard.html', context)

    return render(request, 'error.html', {'message': "You don't have permission to view the dashboard."})

def logincourse(request):
    return render(request,'registration/logincourse.html')

def loginstudent(request):
    return render(request,'registration/loginstudent.html')