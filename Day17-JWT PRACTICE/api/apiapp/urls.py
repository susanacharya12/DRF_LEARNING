from django.urls import path, include
from .views import EmployeeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'student', EmployeeViewSet, basename='student')

urlpatterns = [
    path('', include(router.urls))
    
]
