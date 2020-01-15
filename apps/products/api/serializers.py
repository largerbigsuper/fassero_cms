from rest_framework import serializers
from django.db import transaction
from django.db.models import F


from ..models import (Product, ProductType)

from utils.exceptions import CommonException

class ProductTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductType
        fields = ['id', 'name', 'logo', 'parent', 'level']


class ProductSerializer(serializers.ModelSerializer):

    product_type = ProductTypeSerializer()

    class Meta:
        model = Product
        fields = ['id', 'product_type', 'name', 'cover', 'detail', 'total_left', 'create_at']

