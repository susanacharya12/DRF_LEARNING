from rest_framework.routers import DefaultRouter
from .views import SingerViewSet, SongViewSet
from django.urls import path, include

router = DefaultRouter()

router.register(r'singer', SingerViewSet, basename='singer')
router.register(r'songs', SongViewSet, basename='songs')

urlpatterns = [
    path('', include(router.urls)),
]
