from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated


from ..models import (mm_Product, mm_ProductType,)
from .filters import ProductFilter, ProductTypeFilter
from .serializers import (ProductTypeSerializer, ProductSerializer,)

class ProductTypeViewSet(viewsets.ReadOnlyModelViewSet):

    filter_class = ProductTypeFilter
    serializer_class = ProductTypeSerializer

    def get_queryset(self):
        if self.request.query_params:
            return mm_ProductType.all()
        else:
            return mm_ProductType.top_level_type()



class ProductViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = mm_Product.published_product()
    filter_class = ProductFilter
    serializer_class = ProductSerializer

    @action(detail=False, queryset=mm_Product.recommand_product())
    def recommand(self, request):
        """推荐产品
        """
        return super().list(request)

