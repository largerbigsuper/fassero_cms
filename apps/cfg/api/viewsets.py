from rest_framework import viewsets
from rest_framework.decorators import action

from .serializers import ArticleSerializer
from .filters import ArticleFilter
from ..models import mm_Article


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

