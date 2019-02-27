from django.core.management.base import BaseCommand, CommandError

from pfp.models import (quantitative_Investment, )

class Command(BaseCommand):
    '''
    用于执行周期性获取当日交易数据
    '''
    help = '用户自动周期性获取当天交易数据'

    def handle(self, *args, **options):
        pass