from rest_framework import serializers
from django.db import transaction
from django.db.models import F


from ..models import (Sku, SkuType)

from utils.exceptions import CommonException

class SkuTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = SkuType
        fields = ['id', 'name', 'logo', 'parent', 'level']


class SkuSerializer(serializers.ModelSerializer):

    sku_type = SkuTypeSerializer()

    class Meta:
        model = Sku
        fields = ['id', 'sku_type', 'name', 'cover', 'detail', 'total_left', 'create_at']

