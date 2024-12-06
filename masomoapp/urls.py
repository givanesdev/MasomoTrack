
from django.contrib import admin
from django.urls import path
from masomoapp import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from .views import register_view
from .views import login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('starter/', views.starter, name='starter'),
    path('courses', views.courses, name='courses'),
    path('details', views.details, name='details'),

    path('trainers', views.trainers, name='trainers'),

    path('login/', login_view, name='login'),

    path('register/', register_view, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('members/', views.member_list, name='member_list'),
    path('members/create/', views.member_create, name='member_create'),
    path('members/<int:pk>/update/', views.member_update, name='member_update'),
    path('members/<int:pk>/delete/', views.member_delete, name='member_delete'),

    path('courses/', views.course_list, name='course_list'),
    path('courses/create/', views.course_create, name='course_create'),
    path('courses/<int:pk>/update/', views.course_update, name='course_update'),
    path('courses/<int:pk>/delete/', views.course_delete, name='course_delete'),

    path('students/', views.student_list, name='student_list'),
    path('students/create/', views.student_create, name='student_create'),
    path('students/<int:pk>/update/', views.student_update, name='student_update'),

    path('performances/', views.performance_list, name='performance_list'),
    path('performances/create/', views.performance_create, name='performance_create'),
    path('performances/<int:pk>/update/', views.performance_update, name='performance_update'),
    path('performances/<int:pk>/delete/', views.performance_delete, name='performance_delete'),



    path('dashboard/', views.dashboard, name='dashboard'),

    path('logincourse/', views.logincourse, name='logincourse'),
    path('loginstudent/', views.loginstudent, name='loginstudent'),

]
