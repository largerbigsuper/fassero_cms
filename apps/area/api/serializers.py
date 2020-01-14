from rest_framework import serializers

from ..models import Area


class AreaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Area
        fields = ['id', 'name', 'code']


class AreaParentSerializer(AreaSerializer):
    children = AreaSerializer(many=True)
    
    class Meta:
        model = Area
        fields = ('id', 'code', 'name', 'children')

