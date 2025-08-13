
from django.urls import path
from .views import StudentList

urlpatterns = [
   path('api/', StudentList.as_view(), name='api')
]
