from django.db import models
from django.db.models import F, Sum, aggregates, Q

from django.contrib.auth.models import User as AuthUser
from django.contrib import auth

import time


# Create your models here.

# 资产选项

class ABill(models.Model):
    COIN_RUNNER = (
        ('收入', '收入'),
        ('指出', '指出'),
        ('其他', '其他'),
    )
    b_id = models.CharField('交易单号', max_length=32, null=False, blank=False, default='')
    b_order_id = models.CharField('商家订单号', max_length=125, null=False, blank=False, default='')
    add_time = models.DateTimeField('创建时间', auto_now_add=False)
    trade_create_time = models.DateTimeField('交易创建时间', auto_now_add=False)
    pay_time = models.DateTimeField('付款时间', auto_now=False)
    trade_update_time = models.DateTimeField('交易更新时间', auto_now=False)
    trade_source = models.CharField('交易来源', max_length=32, null=False, blank=True, default='其他')
    trade_type = models.CharField('交易类型', max_length=32, null=False, blank=True, default='')
    trade_user = models.CharField('交易对象', max_length=32, null=False, blank=True, default='其他')
    order_name = models.CharField('商品名称', max_length=255, null=False, blank=False, default='')
    price = models.DecimalField('价格', max_digits=11, decimal_places=2, null=False, blank=False, default=0)
    coin_runner = models.CharField('收/支', max_length=10, choices=COIN_RUNNER, null=False, blank=True, default='其他')
    serve_value = models.DecimalField('服务费', max_digits=11, decimal_places=2, null=False, blank=False, default=0)
    success_refund = models.DecimalField('成功退款', max_digits=11, decimal_places=2, null=False, blank=False, default=0)
    remark = models.CharField('备注', max_length=255, null=False, blank=True, default='')
    coin_stage = models.CharField('资金状态', max_length=255, null=False, blank=True, default='')
    owner = models.ForeignKey(to=AuthUser, on_delete=models.CASCADE, verbose_name='用户', related_name='abill_user')

    class Meta:
        db_table = 'pfp_a_bill'
        verbose_name = '阿里账单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.b_id


class MoneyLineManage(models.Manager):

    def get_income_list_in_month(self, request, *, year=None, mon=None):
        '''
        按照月份获取现金流清单
        如果指定时间，则必须显示指定,年份和月份
        缺省年和月则返回当前月份上月的数据
        :param request:
        :return:
        '''
        if not year or not mon:
            year = time.gmtime().tm_year
            mon = time.gmtime().tm_mon
            if mon == 1:
                year = year - 1
                mon = 12

        queryset = self.all_in_user(user_id=request.user.pk).filter(add_time__year=year,
                                                                    add_time__mon=mon)
        # 找到全部收入的和 减去全部支出的和。得到当月净收入
        return queryset.aggregate(Sum('money_direction', filter=Q(money_direction='2')) - Sum('money_direction',
                                                                                              filter=Q(
                                                                                                  money_direction='1')))

    def all_in_user(self, user_id):
        return self.all().filter(user_id=user_id)


class MoneyLine(models.Model):
    '''
    个人现金流
    需要记录数据：
    收入/指出
    s
    '''
    MONEY_DIRCTION = (
        (1, '支出'),
        (2, '收入'),
        (3, '其他'),
    )
    user = models.ForeignKey(to=auth.models.User, on_delete=models.CASCADE, verbose_name='用户',
                             related_name='money_line_user')
    add_time = models.DateTimeField('添加时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)
    pay_name = models.CharField('账单名称', max_length=255, null=False, blank=False, default='')
    pay_type = models.ForeignKey('PayType', on_delete=models.CASCADE, verbose_name='账单类型')
    pay_num = models.CharField('账单数额', max_length=255, null=False, blank=False, default='')
    money_direction = models.SmallIntegerField('现金流向', choices=MONEY_DIRCTION, null=False,
                                               blank=False, default=3)
    summary = models.CharField('备注', max_length=255, null=False, blank=False, default='')
    pay_time = models.CharField('记账周期', max_length=20, null=False, blank=False, default='01/11-02/10')

    objects = MoneyLineManage

    class Meta:
        verbose_name = '个人现金流主表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.pay_name


class PayType(models.Model):
    '''
    账单类型
    '''

    name = models.CharField('账单类型名称', max_length=255, null=False, blank=False, default='')
    summary = models.CharField('类型描述', max_length=255, null=False, blank=False, default='')
    add_time = models.DateTimeField('添加时间', auto_now_add=True)
    update_time = models.DateTimeField('添加时间', auto_now=True)
    is_must = models.BooleanField('是否必要支出', null=False, blank=False, default=True)

    class Meta:
        verbose_name = '账单类型'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoldListManage(models.Manager):
    def all_in_user(self, user_id):
        return self.filter(user_id=user_id)

    def get_gold_list_in_mon(self, request, *, year=None, mon=None):
        if not year or not mon:
            year = time.gmtime().tm_year
            mon = time.gmtime().tm_mon
            if mon == 1:
                year -= 1
                mon = 12
        queryset = self.all_in_user(request.user.pk).filter(add_time__year=year,
                                                            add_time__mon=mon)

        return queryset


class GoldList(models.Model):
    '''
    个人资产列表

    '''
    user = models.ForeignKey(to=auth.models.User, on_delete=models.CASCADE, verbose_name='用户',
                             related_name='gold_list_user')
    add_time = models.DateTimeField('添加时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)
    name = models.CharField('资产名称', max_length=255, null=False, blank=False, default='')
    summary = models.CharField('资产描述', max_length=255, null=False, blank=False, default='')
    gold_type = models.ForeignKey('GoldType', on_delete=models.CASCADE, verbose_name='资产类型',
                                  related_name='gold_list_type', default=1)

    class Meta:
        verbose_name = '个人资产列表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoldPrice(models.Model):
    '''
    资产价值
    '''

    gold = models.ForeignKey(to='GoldList', on_delete=models.CASCADE, verbose_name='资产', related_name='gold_price_list')
    price = models.DecimalField('资产价值', max_digits=20, decimal_places=5, default=0.00)
    num = models.DecimalField('资产数量', max_digits=20, decimal_places=5, default=1.00)
    one_price = models.DecimalField('资产单价', max_digits=20, decimal_places=5, default=0)
    cost = models.DecimalField('购入成本', max_digits=20, decimal_places=5, default=0)
    profit = models.DecimalField('收益', max_digits=20, decimal_places=5, default=0)
    add_time = models.DateTimeField('添加时间', auto_now_add=True)
    summary = models.CharField('备注', max_length=255, null=False, blank=True, default='')

    class Meta:
        verbose_name = '资产价值'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.gold.name


class GoldType(models.Model):
    '''
    资产类型
    '''
    GOLD_TYPE = (
        ('zc', '资产'),
        ('fz', '负债')
    )
    name = models.CharField('资产类型名称', max_length=255, null=False, blank=False, default='')
    summary = models.CharField('类型描述', max_length=255, null=False, blank=False, default='')
    add_time = models.DateTimeField('添加时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)
    gold_type = models.CharField('资产类型', max_length=10, choices=GOLD_TYPE, null=False, blank=False, default='zc')

    class Meta:
        verbose_name = '资产类型'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
