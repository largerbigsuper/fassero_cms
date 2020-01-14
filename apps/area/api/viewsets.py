from rest_framework import viewsets

from ..models import mm_Area
from .serializers import (AreaSerializer, AreaParentSerializer)
from .filters import AreaFilter
from utils.pagination import Size_Max_Pagination

class AreaViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = AreaSerializer
    filter_class = AreaFilter
    pagination_class = Size_Max_Pagination


    def get_queryset(self):
        if self.request.query_params:
            return mm_Area.all()
        else:
            return mm_Area.province()
