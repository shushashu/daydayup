from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class WeixinUser(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='weixin_user')
    nick_name = models.CharField('微信昵称', max_length=64, null=False, blank=False, default='')
    avatar_url = models.CharField('微信头像', max_length=255, null=False, blank=False, default='default.jpg')
    gender = models.CharField('性别', max_length=1, choices=(
        ('1', '男'),
        ('2', '女'),
        ('0', '未知'),
    ), null=False, blank=False, default='0')
    city = models.CharField('用户所在城市', max_length=255, null=False, blank=False, default='')
    province = models.CharField('用户所在省份', max_length=255, null=False, blank=False, default='')
    country = models.CharField('用户所在国家', max_length=255, null=False, blank=False, default='')
    language = models.CharField('用户语言', max_length=32, choices=(
        ('en', '英文'),
        ('zh_CN', '简体中文'),
        ('zh_TW', '繁体中文'),
    ), null=False, blank=False, default='zh_CN')

    class Meta:
        verbose_name = '微信关联用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nick_name
