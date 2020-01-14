from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated


from ..models import (mm_Sku, mm_SkuType,)
from .filters import SkuFilter, SkuTypeFilter
from .serializers import (SkuTypeSerializer, SkuSerializer,)

class SkuTypeViewSet(viewsets.ReadOnlyModelViewSet):

    filter_class = SkuTypeFilter
    serializer_class = SkuTypeSerializer

    def get_queryset(self):
        if self.request.query_params:
            return mm_SkuType.all()
        else:
            return mm_SkuType.top_level_type()



class SkuViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = mm_Sku.published_sku()
    filter_class = SkuFilter
    serializer_class = SkuSerializer

    @action(detail=False, queryset=mm_Sku.recommand_sku())
    def recommand(self, request):
        """推荐产品
        """
        return super().list(request)

