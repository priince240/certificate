from rest_framework import serializers
from .models import uploads

class api_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=uploads
        fields='__all__'
        
        