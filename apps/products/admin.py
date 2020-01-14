from django.contrib import admin

from .models import (Sku, SkuType)
from .forms import SkuAdminForm

@admin.register(Sku)
class SkuAdmin(admin.ModelAdmin):
    form = SkuAdminForm
    list_display = ['id', 'name', 'cover', 'detail', 'total_left', 'create_at', 'sku_type', 'is_recommand']
    search_fields = ['name']
    ordering = ['order_num', '-create_at']
    autocomplete_fields = ['sku_type']

@admin.register(SkuType)
class SkuTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'logo', 'parent']
    search_fields = ['name']
    autocomplete_fields = ['parent']
