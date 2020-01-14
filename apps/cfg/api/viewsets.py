from rest_framework import viewsets

from .serializers import ArticleSerializer
from .filters import ArticleFilter
from ..models import mm_Article


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    """文章api
    """

    queryset = mm_Article.published_articles()
    serializer_class = ArticleSerializer
    filter_class = ArticleFilter
