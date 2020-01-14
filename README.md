# Fassero 站点

## 初始化项目

```shell
# 创建超级管理员
docker-compose -f compose-production.yml run --rm  django python manage.py createsuperuser

# 初始化地区
docker-compose -f compose-production.yml run --rm  django python manage.py runscript init_area
```