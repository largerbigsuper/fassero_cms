from rest_framework import routers

from apps.area.api.viewsets import AreaViewSet

router = routers.DefaultRouter()
# router.register('users', UserViewSet, 'user')
router.register('area', AreaViewSet, 'api-area')