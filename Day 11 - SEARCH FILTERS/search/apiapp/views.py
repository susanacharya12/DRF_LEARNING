from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Student
from .serializers import StudentSerializer
# from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter

# Create your views here.

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # filter_backends = [SearchFilter]
    # search_fields = ['city', 'name', 'id', 'passby', 'roll']
    filter_backends = [OrderingFilter]
    
    