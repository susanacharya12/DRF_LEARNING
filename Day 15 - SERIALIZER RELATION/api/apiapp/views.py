from django.shortcuts import render
from .models import Singer, Song
from .serializers import SingerSerializer, SongSerializer
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

# Create your views here.
class SingerViewset(viewsets.ModelViewSet):
    queryset = Singer.objects.all().order_by('id') 
    serializer_class = SingerSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'gender']
    
       
class SongViewset(viewsets.ModelViewSet):
    queryset = Song.objects.all().order_by('id')
    serializer_class = SongSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'singer__name'] 
    
    
    