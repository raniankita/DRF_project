from django.contrib import admin
from .models import Student
# Register your models here.
@admin.register(Student)
# to show the data of the student class in the admin panel
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll','city']
