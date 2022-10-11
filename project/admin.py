
from django.contrib import admin
from .models import Employee
# Register your models here.

# admin.site.register(Employee)

class EmployeeAdmin(admin.ModelAdmin):
    list_display=("first_name","second_name","date_of_graduation","date_of_employment",)
    search_fields=("fist_name","second_name","date_of_graduation","date_of_employment",)
admin.site.register(Employee,EmployeeAdmin)
