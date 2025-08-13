from .models import Expense
from .serializers import ExpenseSerializer
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import UpdateAPIView, DestroyAPIView, RetrieveDestroyAPIView,ListCreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView

class ExpenseList(ListAPIView):
    queryset = Expense.objects.all()  
    serializer_class = ExpenseSerializer


class ExpenseCreate(CreateAPIView):
    quertset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    
    
class ExpenseRetrieve(RetrieveAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    
    
class ExpenseUpdate(UpdateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    
    
    
class ExpenseDestroy(DestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    
    

     
class ExpenseListCreate(ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    
    
    
class ExpenseRetrieveUpdate( RetrieveUpdateAPIView):
     queryset = Expense.objects.all()
     serializer_class = ExpenseSerializer
     
     
class ExpenseRetrieveDestroy(RetrieveDestroyAPIView):
     queryset = Expense.objects.all()
     serializer_class = ExpenseSerializer
     
     

class ExpenseRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
     queryset = Expense.objects.all()
     serializer_class = ExpenseSerializer