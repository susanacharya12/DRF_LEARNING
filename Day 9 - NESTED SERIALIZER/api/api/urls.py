from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),       # Admin panel at /admin/
    path('', include('apiapp.urls')),      # Includes all URLs from your 'apiapp' app at root
]
