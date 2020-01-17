from django.contrib import admin
from django.utils.html import mark_safe

from .models import (Product, ProductType, mm_ProductType, ProductTag)
from .forms import ProductAdminForm

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = ['id', 'name', 'cover_image', 'detail', 'total_left', 'create_at', 'product_type', 'is_recommand']
    search_fields = ['name']
    ordering = ['order_num', '-create_at']
    list_filter = ['product_type']
    autocomplete_fields = ['product_tag']

    readonly_fields = ['cover_image']

    def cover_image(self, obj):
        return mark_safe('<img src="{}" width="150" height="150" />'.format(obj.cover))

    cover_image.short_description = '图片'


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'logo_image', 'parent', 'child_product_type', 'lookup_products', 'order_num']
    search_fields = ['name']
    autocomplete_fields = ['parent']
    list_filter = ['parent']

    def get_queryset(self, request):
        if not request.GET:
            return mm_ProductType.get_level_type()
        else:
            return mm_ProductType.all()

    readonly_fields = ['logo_image']

    def logo_image(self, obj):
        return mark_safe('<img src="{}" width="150" height="150" />'.format(obj.logo))

    logo_image.short_description = '图片'

    def child_product_type(self, obj):
        return mark_safe('<a href="?parent__id={}">查看子分类</a>'.format(obj.id))

    child_product_type.short_description = '子分类'

    def lookup_products(self, obj):
        return mark_safe('<a href="/admin/products/product/?product_type={}">查看产品</a>'.format(obj.id))

    lookup_products.short_description = '查看产品'


@admin.register(ProductTag)
class ProductTagAdmin(admin.ModelAdmin):

    list_display = ['id', 'name']
    search_fields = ['name']
    