from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    # 继承自AbstractUser 由于要使用手机注册所以自定义其他字段
    mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号')

    class Meta:
        db_table = 'tb_users'
        verbose_name = '⽤户'
        verbose_name_plural = verbose_name
