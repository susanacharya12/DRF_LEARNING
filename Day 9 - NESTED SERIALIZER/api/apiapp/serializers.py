from rest_framework import serializers
from .models import Songs, Singer

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs           # should be 'model' not 'models'
        fields = ['id', 'title', 'singer']

class SingerSerializer(serializers.ModelSerializer):
    sungby = SongSerializer(many=True, read_only = True)
    class Meta:
        model = Singer          # should be 'model' not 'models'
        fields = ['id', 'name', 'gender', 'sungby']
