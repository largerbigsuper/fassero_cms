from django_filters import rest_framework as filters

from ..models import Article

class ArticleFilter(filters.FilterSet):

    class Meta:
        model = Article
        fields = {
            'site_module': ['exact'],
            'site_module__code': ['exact']
        }