from rest_framework import serializers

from ..models import (SiteModule, Article, IndexItem)

class SiteModuleSerializer(serializers.ModelSerializer):
    """功能模块
    """

    class Meta:
        model = SiteModule
        fields = ['id', 'name', 'code']


class ArticleSerializer(serializers.ModelSerializer):
    """文章详情
    """
    
    site_module = SiteModuleSerializer()

    class Meta:
        model = Article
        fields = ['id', 'site_module', 'title', 'desc', 'cover', 'content', 'link', 'create_at', 'update_at']

class IndexItemSerializer(serializers.ModelSerializer):
    """首页轮播图
    """

    class Meta:
        model = IndexItem
        fields = ['id', 'cover', 'product', 'article']