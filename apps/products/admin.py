from django.contrib import admin
from django.utils.html import mark_safe

from .models import (Product, ProductType)
from .forms import ProductAdminForm

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = ['id', 'name', 'cover', 'detail', 'total_left', 'create_at', 'product_type', 'is_recommand']
    search_fields = ['name']
    ordering = ['order_num', '-create_at']
    autocomplete_fields = ['product_type']

    readonly_fields = ['image_tag']

    def image_tag(self, obj):
        return mark_safe('<img src="{}" width="150" height="150" />'.format(obj.cover))

    image_tag.short_description = '图片'


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'logo', 'parent']
    search_fields = ['name']
    autocomplete_fields = ['parent']
