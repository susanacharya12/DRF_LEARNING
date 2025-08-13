# # from django.shortcuts import render
# # from .models import Student
# # from .serializers import StudentSerializer
# # from django.http import JsonResponse  
# # # Model Objects
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import Quote
# from .serializers import QuoteSerializer

# # # For single student
# # def student_detail(request, pk):
# #     stu = Student.objects.get(id=pk)
# #     serializer = StudentSerializer(stu)
# #     return JsonResponse(serializer.data)  # safe=True by default for dict

# # # For multiple students
# # def student_list(request):
# #     stu = Student.objects.all()
# #     serializer = StudentSerializer(stu, many=True)
# #     return JsonResponse(serializer.data, safe=False)  # required for list



# # def student_city(request):
# #     stu = Student.objects.all()
# #     serializer = StudentSerializer(stu, many=True)
# #     return JsonResponse(serializer.data, safe=False)





# @api_view(['GET','POST'])

# def quote_list(request):
#     if request.method == 'GET':
#         quotes = Quote.objects.all()
#         serializer = QuoteSerializer(quotes, many=True)
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         serializer = QuoteSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
        
#         return Response(serializer.errors, status=400)
            
# @api_view(['GET'])
# def quote_detail(request, pk):
#     try:
#         quote = Quote.objects.get(pk=pk)
#     except Quote.DoesNotExist:
#         return Response({'error': 'Quote not found'}, status=404)

#     serializer = QuoteSerializer(quote)
#     return Response(serializer.data)


# quotes/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Quote
from .serializers import QuoteSerializer

@api_view(['GET', 'POST'])
def quote_list(request):
    if request.method == 'GET':
        quotes = Quote.objects.all()
        serializer = QuoteSerializer(quotes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = QuoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET'])
def quote_detail(request, pk):
    try:
        quote = Quote.objects.get(pk=pk)
    except Quote.DoesNotExist:
        return Response({'error': 'Quote not found'}, status=404)

    serializer = QuoteSerializer(quote)
    return Response(serializer.data)
