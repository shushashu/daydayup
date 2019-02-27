from django.db import models


class Target(models.Model):
    name = models.CharField('标第名称', max_length=32, null=False, blank=False, default='')
    code = models.CharField('标第编码', max_length=32, null=False, blank=False, default='')
    add_time = models.DateTimeField('添加时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)
    remark = models.CharField('标第说明', max_length=255, null=False, blank=False, default='')
    country = models.CharField('所属国家', max_length=255, null=False, blank=False, default='')
    marketplace = models.CharField('所属市场', max_length=255, null=False, blank=False, default='')

    class Meta:
        verbose_name = '标的基础信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class TargetTransaction(models.Model):
    target = models.ForeignKey(to=Target, on_delete=models.CASCADE, verbose_name='标第', related_name='transaction_target')
    date = models.DateTimeField('交易时间', null=False, auto_now=True)
    end_price = models.DecimalField('收盘价', max_digits=10, decimal_places=5, null=False, blank=False, default=0)
    max_price = models.DecimalField('最高价', max_digits=10, decimal_places=5, null=False, blank=False, default=0)
    min_price = models.DecimalField('最高价', max_digits=10, decimal_places=5, null=False, blank=False, default=0)
    start_price = models.DecimalField('最高价', max_digits=10, decimal_places=5, null=False, blank=False, default=0)
    befor_end_price = models.DecimalField('最高价', max_digits=10, decimal_places=5, null=False, blank=False, default=0)
    z_or_d = models.CharField('涨跌额', max_length=15, null=False, blank=False, default='')
    z_or_d_percentage = models.CharField('涨跌幅', max_length=15, null=False, blank=False, default='')
    change_percentage = models.DecimalField('还手率', max_digits=7, decimal_places=4, blank=False, default=0)
    transaction_num = models.BigIntegerField('成交量', null=False, blank=False, default=0)
    transaction_money = models.BigIntegerField('成交金额', null=False, blank=False, default=0)
    target_price = models.BigIntegerField('市值', null=False, blank=False, default=0)
    change_price = models.BigIntegerField('流通市值', null=False, blank=False, default=0)

    class Meta:
        verbose_name = '日交易信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.target.name
