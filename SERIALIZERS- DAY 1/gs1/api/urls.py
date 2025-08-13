# quotes/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('quotes/', views.quote_list, name='quote_list'),
    path('quotes/<int:pk>/', views.quote_detail, name='quote_detail'),
]
