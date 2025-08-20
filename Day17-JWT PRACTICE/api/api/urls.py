from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView, 
    
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apiapp.urls')),
    path('get/', TokenObtainPairView.as_view(), name='get'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('verify/', TokenVerifyView.as_view(), name='verify'),
]
