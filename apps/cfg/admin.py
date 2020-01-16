from django.contrib import admin

from .models import SiteModule, Article
from .forms import ArticleAdminForm

@admin.register(SiteModule)
class SiteModuleAdmin(admin.ModelAdmin):
    """站点模块
    """
    
    list_display = ['id', 'name', 'code', 'parent']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """文章管理
    """
    form = ArticleAdminForm

    list_display = ['id', 'site_module', 'title', 'cover', 'desc', 'create_at', 'status']
    list_filter = ['site_module']
