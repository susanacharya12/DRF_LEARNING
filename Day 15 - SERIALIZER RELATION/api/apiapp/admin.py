from django.contrib import admin
from .models import Singer, Song

# Admin for Singer
@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'gender']
    search_fields = ['name']
    list_filter = ['gender']

# Admin for Song
@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'singer', 'duration']
    search_fields = ['title', 'singer__name']
    list_filter = ['singer', 'duration']
