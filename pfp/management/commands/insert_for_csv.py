import time, os
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from pfp.models import (quantitative_Investment, models as f_models)


class Command(BaseCommand):
    '''
    从csv 格式的文件中导入数据
    '''
    help = '用户自动周期性获取当天交易数据'

    @staticmethod
    def _inspce_date(date):
        return '%s-%s-%s %s:%s:%s' % (
            time.gmtime(date).tm_year,
            time.gmtime(date).tm_mon,
            time.gmtime(date).tm_mday,
            time.gmtime(date).tm_hour,
            time.gmtime(date).tm_min,
            time.gmtime(date).tm_sec,
        )

    def handle(self, *args, **options):
        self.stdout.write('开始导入数据')
        target = quantitative_Investment.Target.objects.all()
        transitc = quantitative_Investment.TargetTransaction.objects.filter(is_active=True)
        with open(os.path.join(settings.BASE_DIR, 'orther_dir', '601788.csv'), 'r', encoding='iso8859') as f:
            for line in f.readlines()[1:]:
                line = line.rstrip('\n').split(',')
                print(line, len(line))
                transitc.create(target=target.filter(code=line[1])[0],
                                date=line[0].replace('/', '-'),
                                end_price=line[3],
                                max_price=line[4],
                                min_price=line[5],
                                start_price=line[6],
                                befor_end_price=line[7],
                                z_or_d=line[8],
                                z_or_d_percentage=line[9],
                                change_percentage=line[10],
                                transaction_num=line[11],
                                transaction_money=line[12],
                                target_price=line[13],
                                change_price=line[14],
                                is_active=True,
                                )
        self.stdout.write('导入数据完成')
