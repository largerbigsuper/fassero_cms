from django_filters import rest_framework as filters

from ..models import Area

class AreaFilter(filters.FilterSet):

    class Meta:
        model = Area
        fields = {
            'code': ['exact'],
            'name': ['exact'],
            'parent': ['exact'],
        }