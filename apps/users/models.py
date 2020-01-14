from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    avatar = models.ImageField(verbose_name='头像')

    class Meta:
        db_table = 'users'
        verbose_name = verbose_name_plural = '用户信息'