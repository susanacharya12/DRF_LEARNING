from django.shortcuts import render
from rest_framework import viewsets
from .models import Songs, Singer
from .serializers import SongSerializer, SingerSerializer

class SingerViewSet(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer

class SongViewSet(viewsets.ModelViewSet):
    queryset = Songs.objects.all()
    serializer_class = SongSerializer

    
