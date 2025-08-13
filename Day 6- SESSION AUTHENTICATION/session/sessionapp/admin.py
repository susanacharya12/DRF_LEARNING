from django.contrib import admin
from .models import School

# Register your models here.
@admin.register(School)

class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name','address','starttime','endtime')