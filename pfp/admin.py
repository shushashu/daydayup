from django.contrib import admin

from pfp import models as f_models

# Register your models here.

admin_site = admin.site


class ABillAdmin(admin.ModelAdmin):
    fields = (
        'b_id',
        'b_order_id',
        'add_time',
        'trade_create_time',
        'pay_time',
        'trade_update_time',
        'trade_source',
        'trade_type',
        'trade_user',
        'order_name',
        'price',
        'coin_runner',
        'serve_value',
        'success_refund',
        'remark',
        'coin_stage',
        'owner',
    )

    list_filter = (
        'b_id', 'trade_user', 'price', 'coin_runner',
    )


admin_site.register(f_models.ABill, ABillAdmin)
admin_site.register(f_models.MoneyLine)
admin_site.register(f_models.GoldList)
admin_site.register(f_models.PayType)
admin_site.register(f_models.GoldType)
admin_site.register(f_models.GoldPrice)
