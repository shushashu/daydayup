from django.contrib import admin
from django.contrib.auth import models

from daydayup.admin_sites import admin_site as admin_site_diy
from pfp import models as f_models

# Register your models here.

admin_site = admin.site


class DayModelAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(user_id=request.user.pk)

    def save_model(self, request, obj, form, change):
        obj.user = models.User.objects.get(id=request.user.pk)
        super().save_model(request, obj, form, change)


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


class MoneyLineAdmin(DayModelAdmin):
    fields = (
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
        'num',
        'one_price',
        'cost',
        'profit',
        'summary',
    )

    extra = 0
    ordering = ('-add_time',)


class GoldListAdmin(DayModelAdmin):
    fields = (
        'name',
        'gold_type',
        'summary',
    )

    list_filter = (
        'name', 'gold_type'
    )

    list_display = (
        'name',
        'gold_type',
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
admin_site.register(model_or_iterable=f_models.MoneyLine, admin_class=MoneyLineAdmin)
admin_site.register(f_models.GoldList, GoldListAdmin)
admin_site.register(f_models.PayType, PayTypeAdmin)
admin_site.register(f_models.GoldType)
admin_site.register(f_models.GoldPrice)
