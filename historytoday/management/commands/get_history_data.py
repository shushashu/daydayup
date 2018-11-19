'''
用来通过接口获取 历史上的今天的数据
autor : heroHu
time  : 2018/11/19
'''

import time

from django.core.management.base import BaseCommand, CommandError
from historytoday import models as hm
from . import tasks

class Command(BaseCommand):
    help = '拉去历史上的今天的数据'

    def handle(self, *args, **options):
        self.stdout.write('开始拉去信息')
        tasks.save_story_db(date=time.localtime(time.time()))
        self.stdout.write('信息拉去完成')
