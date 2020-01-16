from django.db import models

from mptt.models import MPTTModel, TreeForeignKey

from utils.modelmanager import ModelManager

class SiteModuleManager(ModelManager):
    pass

class SiteModule(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    code = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    objects = SiteModuleManager()

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        db_table = 'cms_site_module'
        verbose_name = '站点模块'
        verbose_name_plural = '站点模块'
    
    def __str__(self):
        return self.name

mm_SiteModule = SiteModule.objects

class ArticleManager(ModelManager):

    STATUS_EDITING = 0
    STATUS_PUBLISHED = 1
    STATUS_REVOKE = 2
    ARTICLE_STATUS = (
        (STATUS_EDITING, '编辑中'),
        (STATUS_PUBLISHED, '已发布'),
        (STATUS_REVOKE, '已撤回'),
    )

    def published_articles(self):
        """已发布文章
        """
        return self.filter(status=self.STATUS_PUBLISHED)

    def recommand_articles(self):
        """推荐文章
        """
        return self.published_articles().filter(is_recommand=True)


class Article(models.Model):
    """站点说明
    """

    site_module = models.ForeignKey(SiteModule, on_delete=models.CASCADE, null=True, blank=True, verbose_name='站点模块')
    title = models.CharField(max_length=150, default='', verbose_name='标题')
    desc = models.CharField(max_length=500, default='', verbose_name='简介')
    cover = models.ImageField(verbose_name='封面图')
    content = models.TextField(verbose_name='内容')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    status = models.PositiveSmallIntegerField(choices=ArticleManager.ARTICLE_STATUS,
        default=ArticleManager.STATUS_EDITING,
        verbose_name='状态')
    is_recommand = models.BooleanField(default=False, verbose_name='推荐')

    objects = ArticleManager()

    class Meta:
        db_table = 'cms_article'
        ordering = ['-id']
        verbose_name = '文章'
        verbose_name_plural = '文章'

    def __str__(self):
        return self.title

mm_Article = Article.objects
