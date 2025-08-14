from django.shortcuts import render
from rest_framework import viewsets
from .models import Hostel
from .serializers import HostelSerializer
from rest_framework.filters import SearchFilter

# Create your views here.

class HostelViewSet(viewsets.ModelViewSet):
    queryset = Hostel.objects.all()
    serializer_class = HostelSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'location', 'owner']

    
    
