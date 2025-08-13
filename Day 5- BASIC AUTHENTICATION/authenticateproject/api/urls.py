from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentModelViewSet

router = DefaultRouter()
router.register(r'students', StudentModelViewSet, basename='student')

urlpatterns = [
    path('', include(router.urls)),
]
