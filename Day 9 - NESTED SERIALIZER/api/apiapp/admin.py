from django.contrib import admin
from .models import Singer, Songs

@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    list_display = ['name', 'gender']  # Columns shown in the Singer list page

@admin.register(Songs)
class SongsAdmin(admin.ModelAdmin):
    list_display = ['title', 'singer']  # Columns shown in the Songs list page
