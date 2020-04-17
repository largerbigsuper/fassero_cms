from django.contrib import admin
from django.utils.html import mark_safe
from django.db import models

from .models import SiteModule, Article, IndexItem
from .forms import ArticleAdminForm
from django.forms.widgets import TextInput

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

    list_display = ['id', 'site_module', 'title', 'cover_image', 'desc', 'create_at', 'status']
    list_filter = ['site_module']
    search_fields = ['title']
    readonly_fields = ['cover_image']

    def cover_image(self, obj):
        return mark_safe('<img src="{}" width="150" height="150" />'.format(obj.cover))

    cover_image.short_description = '图片'

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'120'})},
    }

@admin.register(IndexItem)
class IndexItemAdmin(admin.ModelAdmin):
    """首页轮播设置
    """
    list_display = ['id', 'cover_image', 'product', 'article', 'order_num', 'create_at', 'update_at']

    autocomplete_fields = ['product', 'article']

    readonly_fields = ['cover_image']

    def cover_image(self, obj):
        return mark_safe('<img src="{}" width="150" height="150" />'.format(obj.cover))

    cover_image.short_description = '图片'

