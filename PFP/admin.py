from django.contrib import admin

from PFP.models import ABill

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


admin_site.register(ABill, ABillAdmin)
