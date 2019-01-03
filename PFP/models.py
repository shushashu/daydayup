from django.db import models

from django.contrib.auth.models import User as AuthUser

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
    add_time = models.DateTimeField('创建时间', auto_now_add=True)
    trade_create_time = models.DateTimeField('交易创建时间', null=False, blank=False, auto_now_add=False)
    pay_time = models.DateTimeField('付款时间', null=False, blank=False, auto_now=False)
    trade_update_time = models.DateTimeField('交易更新时间', null=False, blank=False, auto_now=False)
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


