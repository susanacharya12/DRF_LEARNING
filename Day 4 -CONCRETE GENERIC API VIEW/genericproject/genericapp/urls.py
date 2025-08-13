from .views import ExpenseList, ExpenseCreate, ExpenseRetrieve, ExpenseUpdate, ExpenseDestroy, ExpenseRetrieveDestroy, ExpenseListCreate, ExpenseRetrieveUpdate,ExpenseRetrieveUpdateDestroy
from django.urls import path

urlpatterns = [
    path('expenses/', ExpenseList.as_view(), name='expense-list'),
    path('expensecreate/', ExpenseCreate.as_view(), name='expense-list'),
    path('expense/<int:pk>/', ExpenseRetrieve.as_view(), name='expense'),
    path('update/<int:pk>/', ExpenseUpdate.as_view(), name='expense-update'),
    path('destroy/<int:pk>/', ExpenseDestroy.as_view(), name='expense-destroy'),
    path('retrievedestroy/<int:pk>/', ExpenseRetrieveDestroy.as_view(), name='expense-retrievedestroy'),
    path('listcreate/', ExpenseListCreate.as_view(), name='listcreate'),
    path('retreiveupdate/<int:pk>/', ExpenseRetrieveUpdate.as_view(), name='listcreate'),
    path('retrieveupdatedestroy/<int:pk>/', ExpenseRetrieveUpdateDestroy.as_view(), name='listcreate'),
    
            
]

