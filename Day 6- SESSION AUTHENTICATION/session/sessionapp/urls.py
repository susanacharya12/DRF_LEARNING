from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SchoolViewSet

router = DefaultRouter()

router.register(r'school', SchoolViewSet, basename = 'school')


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace = 'rest_framework'))
]

