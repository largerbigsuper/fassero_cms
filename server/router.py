from rest_framework import routers

from apps.cfg.api.viewsets import ArticleViewSet

router = routers.DefaultRouter()

router.register('article', ArticleViewSet, 'api-article')