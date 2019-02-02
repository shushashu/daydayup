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


class MoneyLineAdmin(admin.ModelAdmin):
    fields = (
        'user',
        'pay_name',
        'pay_type',
        'pay_num',
        'money_direction',
        'pay_time',
        'summary'
    )

    list_filter = (
        'pay_name',
        'pay_type',
        'pay_num',
        'money_direction',
        'pay_time'
    )

    list_display = (
        'pay_name',
        'pay_num',
        'pay_type',
        'money_direction',
        'summary'
    )

    list_editable = (
        'summary',
    )


class GoldPriceTabularInline(admin.TabularInline):
    model = f_models.GoldPrice
    fields = (
        'price',
    )

    extra = 0


class GoldListAdmin(admin.ModelAdmin):
    fields = (
        'user',
        'name',
        'gold_type',
        'summary',
    )

    list_filter = (
        'name', 'summary'
    )

    list_display = (
        'name',
        'summary'
    )

    inlines = [
        GoldPriceTabularInline,
    ]


class PayTypeAdmin(admin.ModelAdmin):
    fields = (
        'name',
        'summary',
        'is_must'
    )


admin_site.register(f_models.ABill, ABillAdmin)
admin_site.register(f_models.MoneyLine, MoneyLineAdmin)
admin_site.register(f_models.GoldList, GoldListAdmin)
admin_site.register(f_models.PayType, PayTypeAdmin)
admin_site.register(f_models.GoldType)
admin_site.register(f_models.GoldPrice)
