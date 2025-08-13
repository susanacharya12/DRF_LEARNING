from django.shortcuts import render
from .serializers import EventSerializer
from rest_framework import viewsets
from rest_framework import viewsets
from .models import Event

# Create your views here.
class EventModelViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    
    
    
    