from django_filters import rest_framework as filters

from ..models import ProductType, Product

class ProductTypeFilter(filters.FilterSet):

    class Meta:
        model = ProductType
        fields = {
            'parent': ['exact'],
            'level': ['exact'],
        }


class ProductFilter(filters.FilterSet):

    class Meta:
        model = Product
        fields = {
            'product_type': ['exact'],
            'is_recommand': ['exact'],
            'name': ['contains'],
            'detail': ['contains'],
        }