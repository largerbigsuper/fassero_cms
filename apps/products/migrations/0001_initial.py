# Generated by Django 3.0.2 on 2020-01-15 01:17

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SkuType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, unique=True, verbose_name='类型')),
                ('logo', models.ImageField(blank=True, upload_to='', verbose_name='封面图')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='products.SkuType')),
            ],
            options={
                'verbose_name': '商品类型',
                'verbose_name_plural': '商品类型',
                'db_table': 'cms_sku_type',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Sku',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='商品名')),
                ('cover', models.ImageField(upload_to='', verbose_name='封面图')),
                ('detail', models.TextField(blank=True, default='', verbose_name='详情')),
                ('total_left', models.PositiveIntegerField(blank=True, default=0, verbose_name='总量')),
                ('total_sales', models.PositiveIntegerField(blank=True, default=0, verbose_name='销量')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, '编辑中'), (1, '已上架'), (2, '已下架')], default=0, verbose_name='兑换商品状态')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('order_num', models.IntegerField(default=10000, verbose_name='排序值[越小越靠前]')),
                ('is_recommand', models.BooleanField(blank=True, default=False, verbose_name='推荐')),
                ('sku_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.SkuType', verbose_name='类型')),
            ],
            options={
                'verbose_name': '商品',
                'verbose_name_plural': '商品',
                'db_table': 'cms_sku',
                'ordering': ['order_num', '-create_at'],
            },
        ),
    ]
