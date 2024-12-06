from django.contrib import admin
from .models import Course, Student, Performance, Member

# Register your models here.
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Performance)
admin.site.register(Member)

