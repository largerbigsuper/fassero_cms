from datetime import datetime
from random import random

from django.db import models
from django.db.models import F
from django.conf import settings
from mptt.models import MPTTModel, TreeForeignKey

from utils.modelmanager import ModelManager

class ProductTagManager(ModelManager):
    pass

class ProductTag(models.Model):

    name = models.CharField(max_length=20, unique=True,verbose_name='标签名')

    objects = ProductTagManager()

    class Meta:
        db_table = 'cms_product_tag'
        ordering = ['-id']
        verbose_name = '产品标签'
        verbose_name_plural = '产品标签'
    
    def __str__(self):
        return self.name

mm_ProductTag = ProductTag.objects


class ProductTypeManager(ModelManager):
    
    def get_level_type(self, level=0):
        """一级分类
        """
        return self.filter(level=level)


class ProductType(MPTTModel):
    name = models.CharField(max_length=20, unique=True, db_index=True, verbose_name='类型')
    logo = models.ImageField(blank=True, verbose_name='封面图')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    order_num = models.IntegerField(default=10000, verbose_name='排序值[越小越靠前]')

    objects = ProductTypeManager()

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        db_table = 'cms_product_type'
        ordering = ['level', 'order_num', 'id']
        verbose_name = '产品类型'
        verbose_name_plural = '产品类型'

    def __str__(self):
        return self.name

mm_ProductType = ProductType.objects


class ProductManager(ModelManager):

    STATUS_EDITING = 0
    STATUS_PUBLISHED = 1
    STATUS_RECALL = 2

    STATUS_CHOICES = [
        (STATUS_EDITING, '编辑中'),
        (STATUS_PUBLISHED, '已上架'),
        (STATUS_RECALL, '已下架')
    ]

    def published_product(self):
        """在售产品
        """
        return self.filter(status=self.STATUS_PUBLISHED)
    
    def recommand_product(self):
        """推荐产品
        """
        return self.published_product().filter(is_recommand=True)

    def update_data(self, pk, field_name, amount=1):
        if amount > 0: 
            value = F(field_name) + amount
        else:
            value = F(field_name) - abs(amount)
        updates = {
            field_name: value
        }
        self.filter(pk=pk).update(**updates)

class Product(models.Model):
    """产品
    """

    product_type = models.ForeignKey(ProductType, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='类型')
    name = models.CharField(max_length=120, verbose_name='产品名')
    cover = models.ImageField(verbose_name='封面图')
    detail = models.TextField(default='', blank=True, verbose_name='详情')
    total_left = models.PositiveIntegerField(default=0, blank=True, verbose_name='总量')
    total_sales = models.PositiveIntegerField(default=0, blank=True, verbose_name='销量')
    status = models.PositiveSmallIntegerField(choices=ProductManager.STATUS_CHOICES,
                                            default=ProductManager.STATUS_EDITING,
                                            verbose_name='兑换产品状态')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    order_num = models.IntegerField(default=10000, verbose_name='排序值[越小越靠前]')
    is_recommand = models.BooleanField(default=False, blank=True, verbose_name='推荐')
    product_tag = models.ManyToManyField(ProductTag, related_name='tags', db_table='cms_product_product_tag', blank=True, verbose_name='产品标签')
    
    objects = ProductManager()

    class Meta:
        db_table = 'cms_product'
        ordering = ['order_num', '-create_at']
        verbose_name  = '产品'
        verbose_name_plural  = '产品'

    def __str__(self):
        return self.name

mm_Product = Product.objects

