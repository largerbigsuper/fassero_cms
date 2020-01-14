# 初始化站点功能
# python manage.py runscript init_site

from apps.cfg.models import SiteModule, mm_SiteModule


def init_site_modules():
    """初始化站点功能
    """
    top_modules = []
    names = [
        ('企业特色', 1),
        ('企业理念和发展规划', 2),
        ('企业团队', 3),
        ('合作案例', 4), 
        ('联系/加入我们', 5)
    ]
    for name, code in names:
        SiteModule(name=name, code=code).save()

def run():
    init_site_modules()