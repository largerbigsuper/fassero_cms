from rest_framework import viewsets
from rest_framework.decorators import action

from .serializers import ArticleSerializer, IndexItemSerializer
from .filters import ArticleFilter
from ..models import mm_Article, mm_IndexItem


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    """文章api
    """

    queryset = mm_Article.published_articles()
    serializer_class = ArticleSerializer
    filter_class = ArticleFilter

    @action(detail=False, queryset=mm_Article.recommand_articles())
    def recommand(self, request):
        """推荐阅读
        """
        return super().list(request)


class IndexItemViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = mm_IndexItem.all()
    serializer_class = IndexItemSerializer
