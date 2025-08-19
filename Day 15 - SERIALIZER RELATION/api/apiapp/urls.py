from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SingerViewset, SongViewset


router = DefaultRouter()

router.register(r'singer', SingerViewset, basename='singer')
router.register(r'song', SongViewset, basename='song')

urlpatterns = [
    path('', include(router.urls))
   
]