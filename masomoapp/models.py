from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    teacher = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.CharField(max_length=100)  # String to store the user info
    date_of_birth = models.DateField()

    def __str__(self):
        return self.user

class Performance(models.Model):
    student = models.CharField(max_length=100)  # String to store student info
    course = models.CharField(max_length=100)  # String to store course info
    grade = models.CharField(max_length=2)  # A, B, C, etc.
    score = models.FloatField()

    def __str__(self):
        return f'{self.student} - {self.course}'


class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    role = models.CharField(max_length=50, default='member')  # Default role is 'member'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"











