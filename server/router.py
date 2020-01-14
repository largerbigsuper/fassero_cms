from rest_framework import routers

from apps.cfg.api.viewsets import ArticleViewSet
from apps.products.api import viewsets as products_viewsets

router = routers.DefaultRouter()

router.register('article', ArticleViewSet, 'api-article')
router.register('sku_type', products_viewsets.SkuTypeViewSet, 'api-sku-type')
router.register('sku', products_viewsets.SkuViewSet, 'api-sku')