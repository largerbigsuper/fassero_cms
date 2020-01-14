from datetime import datetime
from random import random

from django.db import models
from django.db.models import F
from django.conf import settings
from mptt.models import MPTTModel, TreeForeignKey

from utils.modelmanager import ModelManager


class SkuTypeManager(ModelManager):
    
    def top_level_type(self):
        """一级分类
        """
        return self.filter(level=0)
        

class SkuType(MPTTModel):
    name = models.CharField(max_length=20, unique=True, db_index=True, verbose_name='类型')
    logo = models.ImageField(blank=True, verbose_name='封面图')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    objects = SkuTypeManager()

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        db_table = 'cms_sku_type'
        ordering = ['-id']
        verbose_name = '产品类型'
        verbose_name_plural = '产品类型'

    def __str__(self):
        return self.name

mm_SkuType = SkuType.objects


class SkuManager(ModelManager):

    STATUS_EDITING = 0
    STATUS_PUBLISHED = 1
    STATUS_RECALL = 2

    STATUS_CHOICES = [
        (STATUS_EDITING, '编辑中'),
        (STATUS_PUBLISHED, '已上架'),
        (STATUS_RECALL, '已下架')
    ]

    def published_sku(self):
        """在售产品
        """
        return self.filter(status=self.STATUS_PUBLISHED)
    
    def recommand_sku(self):
        """推荐产品
        """
        return self.published_sku().filter(is_recommand=True)

    def update_data(self, pk, field_name, amount=1):
        if amount > 0: 
            value = F(field_name) + amount
        else:
            value = F(field_name) - abs(amount)
        updates = {
            field_name: value
        }
        self.filter(pk=pk).update(**updates)

class Sku(models.Model):
    """产品
    """

    sku_type = models.ForeignKey(SkuType, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='类型')
    name = models.CharField(max_length=120, verbose_name='产品名')
    cover = models.ImageField(verbose_name='封面图')
    detail = models.TextField(default='', blank=True, verbose_name='详情')
    total_left = models.PositiveIntegerField(default=0, blank=True, verbose_name='总量')
    total_sales = models.PositiveIntegerField(default=0, blank=True, verbose_name='销量')
    status = models.PositiveSmallIntegerField(choices=SkuManager.STATUS_CHOICES,
                                            default=SkuManager.STATUS_EDITING,
                                            verbose_name='兑换产品状态')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    order_num = models.IntegerField(default=10000, verbose_name='排序值[越小越靠前]')
    is_recommand = models.BooleanField(default=False, blank=True, verbose_name='推荐')
    
    objects = SkuManager()

    class Meta:
        db_table = 'cms_sku'
        ordering = ['order_num', '-create_at']
        verbose_name  = '产品'
        verbose_name_plural  = '产品'

    def __str__(self):
        return self.name

mm_Sku = Sku.objects


# class SkuPropertyNameManager(ModelManager):
#     pass

# class SkuPropertyName(models.Model):
#     """产品属性名称
#     """
    
#     name = models.CharField(max_length=20, unique=True, db_index=True, verbose_name='属性名称')

#     objects = SkuPropertyNameManager()

#     class Meta:
#         db_table = 'cms_sku_property_name'
#         ordering = ['-id']
#         verbose_name = '产品属性名'
#         verbose_name_plural = '产品属性名'


# mm_SkuPropertyName = SkuPropertyName.objects

# class SkuPropertyManager(ModelManager):
#     pass


# class SkuProperty(models.Model):
#     """产品属性
#     """
#     sku = models.ForeignKey(Sku, on_delete=models.CASCADE, related_name='sku_properties', verbose_name='产品')
#     property_name_1 = models.CharField(max_length=20, verbose_name='属性名')
#     property_value_1 = models.CharField(max_length=20, verbose_name='属性值')
#     property_name_2 = models.CharField(max_length=20, null=True, blank=True, verbose_name='属性名2')
#     property_value_2 = models.CharField(max_length=20, null=True, blank=True, verbose_name='属性值2')
#     property_name_3 = models.CharField(max_length=20, null=True, blank=True, verbose_name='属性名3')
#     property_value_3 = models.CharField(max_length=20,null=True, blank=True, verbose_name='属性值3')
#     total_left = models.PositiveIntegerField(default=0, blank=True, verbose_name='总量')
#     total_sales = models.PositiveIntegerField(default=0, blank=True, verbose_name='销量')
#     create_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
#     update_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
#     objects = SkuPropertyManager()

#     class Meta:
#         db_table = 'cms_sku_property'
#         ordering = ['-id']
#         verbose_name = '产品属性'
#         verbose_name_plural = '产品属性'

#     def __str__(self):
#         descprition = self.property_name_1 + ': ' + self.property_value_1 + ' '
#         if self.property_name_2 and self.property_value_2:
#             descprition += self.property_name_2 + ': ' + self.property_value_2 + ' '
#         if self.property_name_3 and self.property_value_3:
#             descprition += self.property_name_3 + ': ' + self.property_value_3 + ' '
#         return descprition
 
# mm_SkuProperty = SkuProperty.objects

