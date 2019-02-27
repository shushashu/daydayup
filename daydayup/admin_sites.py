from django.apps import apps
from django.contrib import admin
from django.template.response import TemplateResponse
from django.utils.functional import LazyObject
from django.utils.module_loading import import_string
from django.views.decorators.cache import never_cache

import time

from pfp.models.models import GoldList, MoneyLine


class AdminSite(admin.AdminSite):

    @never_cache
    def index(self, request, extra_context=None):
        '''
        自定义 登陆页面首页。
        :param request:
        :param extra_context:
        :return:
        '''
        # 原始 index 需要展示数据
        app_list = self.get_app_list(request)

        context = {
            **self.each_context(request),
            'title': self.index_title,
            'app_list': app_list,
            **(extra_context or {}),
        }

        request.current_app = self.name

        # context.update(dict(money_line_income_list=MoneyLine.objects.get_income_list_in_month(request)))
        request.current_app = self.name

        return TemplateResponse(request, self.index_template or 'admin/index.html', context)


admin_site = AdminSite()
