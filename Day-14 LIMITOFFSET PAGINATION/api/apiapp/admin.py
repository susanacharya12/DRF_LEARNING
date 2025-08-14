from django.contrib import admin
from .models import Hostel

@admin.register(Hostel)
class HostelAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "owner", "room_type", "fee")
    list_filter = ("location", "room_type")
    search_fields = ("name", "owner")
