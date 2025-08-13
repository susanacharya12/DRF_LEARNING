from django.contrib import admin
from .models import Quote

# # # Register your models here.
# # @admin.register(Student)
# # class StudentAdmin(admin.ModelAdmin):
# #     list_display = ['id','name','roll','city']

@admin.register(Quote)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['text','author','created_at']