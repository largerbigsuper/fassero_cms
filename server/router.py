from rest_framework import routers

from apps.cfg.api.viewsets import ArticleViewSet
from apps.products.api import viewsets as products_viewsets
from apps.users.api import viewsets as user_viewsets

router = routers.DefaultRouter()

router.register('user', user_viewsets.UserViewSet, 'api-user')
router.register('article', ArticleViewSet, 'api-article')
router.register('product_type', products_viewsets.ProductTypeViewSet, 'api-product-type')
router.register('product', products_viewsets.ProductViewSet, 'api-product')