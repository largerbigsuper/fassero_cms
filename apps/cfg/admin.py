from django.contrib import admin
from django.utils.html import mark_safe

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

    readonly_fields = ['image_tag']

    def image_tag(self, obj):
        return mark_safe('<img src="{}" width="150" height="150" />'.format(obj.cover))

    image_tag.short_description = '图片'

