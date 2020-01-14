from django_filters import rest_framework as filters

from ..models import SkuType, Sku

class SkuTypeFilter(filters.FilterSet):

    class Meta:
        model = SkuType
        fields = {
            'parent': ['exact'],
            'level': ['exact'],
        }


class SkuFilter(filters.FilterSet):

    class Meta:
        model = Sku
        fields = {
            'sku_type': ['exact'],
            'is_recommand': ['exact'],
            'name': ['contains'],
            'detail': ['contains'],
        }