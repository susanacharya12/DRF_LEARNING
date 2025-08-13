from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Include the students app URLs under api/ (or any prefix you want)
    path('api/', include('students.urls')),  
]
