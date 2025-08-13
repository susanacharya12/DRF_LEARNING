from rest_framework.routers import DefaultRouter
from .views import EventModelViewSet
from django.urls import path, include


router = DefaultRouter()


router.register('event', EventModelViewSet, basename='Event')



urlpatterns = [
    path('',include(router.urls))
   
    
]