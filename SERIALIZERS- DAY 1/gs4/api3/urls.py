# urls.py
from django.urls import path
from .views import StudentListCreateAPIView, StudentDetailUpdateDeleteAPIView

urlpatterns = [
    path('students/', StudentListCreateAPIView.as_view(), name='student-list-create'),
    path('students/<int:pk>/', StudentDetailUpdateDeleteAPIView.as_view(), name='student-detail-update-delete'),
]
