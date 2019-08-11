'''
:author heroHu
:time   2019/08/04
:fun    公司全景图 模型表单
'''

from django.db import models
from django.db.models.functions import Now
from django.contrib.auth.models import User


class CompanyModel(models.Model):
    '''
    公司基本信息表
    用于存储公司基本信息
    '''
    name = models.CharField('公司名称', max_length=255, null=False, blank=False, default='')
    com_id = models.CharField('公司信用代码', max_length=255, null=False, blank=False, default='')
    negotiable_securities_id = models.CharField('公司股票代码', max_length=255, null=False, blank=True, default='')
    service = models.TextField('公司主要业务', max_length=1024, null=False, blank=True, default='')
    trade = models.ForeignKey('TradeMode', on_delete=models.CASCADE, verbose_name='所属行业')
    region = models.CharField('公司主要业务区域', max_length=255, null=False, blank=True, default='')
    address = models.CharField('公司地址', max_length=255, null=False, blank=True, default='')
    email = models.EmailField('公司电邮', null=False, blank=True, default='')
    phone = models.CharField('公司电话', max_length=255, null=False, blank=True, default='')
    manager = models.ManyToManyField(verbose_name='公司高管', to='ManagerModel')
    create_at = models.DateTimeField('创建时间', auto_now_add=True)
    update_at = models.DateTimeField('修改时间', auto_now=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='编辑人')


class ManagerModel(models.Model):
    '''
    公司高管人员信息表
    '''
    name = models.CharField('姓名', max_length=255, null=False, blank=False, default='')
    age = models.IntegerField('年龄', default=-1)
    native_place = models.CharField('籍贯', max_length=255, null=False, blank=True, default='')
    experience = models.TextField('履历', null=False, blank=True, default='', max_length=1024)
    enable = models.BooleanField('是否可用', null=False, default=True)
    birthday = models.DateTimeField('出生日期', null=False, blank=True, default=Now)
    phone = models.CharField('电话', max_length=255, null=False, blank=True, default='')
    create_at = models.DateTimeField('创建时间', auto_now_add=True)
    update_at = models.DateTimeField('修改时间', auto_now=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='编辑人')

    class Meta:
        verbose_name = '公司高管人员信息表'
        verbose_name_plural = verbose_name


class TradeMode(models.Model):
    '''
    公司行业分类
    '''
    name = models.CharField('行业名称', max_length=255, null=False, blank=False, default='')
    tags = models.CharField('行业标签', max_length=255, null=False, blank=True, default='')
    enable = models.BooleanField('是否有效', null=False, default=True)
    create_at = models.DateField('创建时间', auto_now_add=True)
    guild = models.TextField('行业协会信息', max_length=1024, null=False, blank=False, default='')
    update_at = models.DateTimeField('修改时间', auto_now=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='编辑人')

    class Meta:
        verbose_name = '公司行业分类'
        verbose_name_plural = verbose_name


class FinanceAllInModel(models.Model):
    '''
    公司财务数据 全景表
    '''

    company = models.ForeignKey('CompanyModel', on_delete=models.CASCADE, verbose_name='公司名称')
    name = models.CharField('财务数据名称', max_length=255, null=False, blank=False, default='')
    value = models.IntegerField('财务数据值', null=False, blank=False, default=-1)
    year = models.DateField(verbose_name='数据时间', auto_now_add=True)
    enable = models.BooleanField('是否有效', null=False, blank=False, default=True)
    create_at = models.DateTimeField('记录创建时间', auto_now_add=True)
    update_at = models.DateTimeField('更新时间', auto_now=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='编辑人')

    class Meta:
        verbose_name = '公司财务数据 全景表'
        verbose_name_plural = verbose_name


class SharesModel(models.Model):
    '''
    公司前十名股东列表,包括历史前十名以及当前前10名
    '''
    company = models.ForeignKey('CompanyModel', on_delete=models.CASCADE, verbose_name='公司')
    name = models.CharField('股东名称', max_length=255, null=False, default='')
    # 如果是机构股东填写company id， 如果自然人股东填写 manager id
    share_id = models.CharField('股东ID', max_length=255, null=False, default='-1', blank=True)
    subclass = models.CharField('股东类型', choices=(
        ('自认人股东', '自然人'),
        ('机构股东', '机构股东'),
        ('其他类型', '其他类型')
    ), max_length=32, null=False, default='其他类型')
    now_num = models.IntegerField('当前持有数量', null=False, blank=True, default=-1)
    ship_subclass = models.CharField('持股类型', choices=(
        ('流通股', '流通顾'),
        ('限制性股票', '限制性股票'),
        ('其他类型', '其他类型')
    ), max_length=32, null=False, blank=False, default='流通股')
    short = models.IntegerField('股东排名', null=False, blank=True, default=-1)
    enable = models.BooleanField('是否有效', default=True)
    create_at = models.DateTimeField('创建时间', auto_now_add=True)
    update_at = models.DateTimeField('修改时间', auto_now=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='编辑人')

    class Meta:
        verbose_name = '公司前十名股东'
        verbose_name_plural = verbose_name


class SharesNumModel(models.Model):
    shares = models.ForeignKey('SharesModel', on_delete=models.CASCADE, verbose_name='股东')
    num = models.IntegerField('持股数量', null=False, blank=True, default=-1)
    having_time = models.DateTimeField('持股时间')
    create_at = models.DateTimeField('创建时间', auto_now_add=True)
    update_at = models.DateTimeField('修改时间', auto_now=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='编辑人')

    class Meta:
        verbose_name = '历史持股数据'
        verbose_name_plural = verbose_name
