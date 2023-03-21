from django.contrib import admin
from .models import Employee
# Register your models here.

@admin.register(Employee)
class EmpolyeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'department', 'post', 'cnic', 'contact', 'city']