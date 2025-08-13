from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.student_list_create, name='student-list-create'),
    path('students/<int:pk>/', views.student_detail, name='student-detail'),
    path('student/', views.student_detail, name='student-detail'),

]
