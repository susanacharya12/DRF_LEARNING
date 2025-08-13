# from rest_framework import serializers
# from .models import Quote

# # class StudentSerializer(serializers.Serializer):
# #     name = serializers.CharField(max_length=100)
# #     roll = serializers.IntegerField()
# #     city = serializers.CharField(max_length=100)
    
    
# class QuoteSerializer(serializers.Serializer):
#      class Meta:
#          model = Quote
#          fields = '__all__'

# quotes/serializers.py

from rest_framework import serializers
from .models import Quote

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'
