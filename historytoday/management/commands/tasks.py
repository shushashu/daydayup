'''
爬虫 获取更新获取历史上的今天发生的事件的数据
outor：  herohu
time：   2018/11/15
email：  gmclqb@163.com
'''

import time
import json
import requests

from historytoday.models import *

__all__ = ['save_story_db']

KEY = '579c7f86b6894182cdc8bfcd2b034f22'
VERSION = '1.0'
URL = "http://v.juhe.cn/todayOnhistory/queryEvent.php"
URL_INFO = 'http://v.juhe.cn/todayOnhistory/queryDetail.php'


def get_history_story_list(url, month, day):
    '''
    获取 时间列表
    :param url:
    :param month:
    :param day:
    :return:
    '''
    querystring = {"key": KEY, "date": '%s/%s' % (month, day)}

    headers = {
        'cache-control': "no-cache",
        'postman-token': "783af053-70e6-f705-71cc-4ba93aadbfc0"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    resp = json.loads(response.text)
    if resp.get('error_code') == 0:
        return resp.get('result')

    else:
        raise ValueError('数据聚合接口返回数据错误')


def get_history_story_info(url, story_id):
    '''
    获取 事件详情
    :param url:
    :param story_id:
    :return:
    '''
    querystring = {'key': KEY, 'e_id': story_id}

    headers = {
        'cache-control': "no-cache",
        'postman-token': "783af053-70e6-f705-71cc-4ba93aadbfc0"
    }

    response = requests.request('GET', url, headers=headers, params=querystring)
    resp = json.loads(response.text)
    if resp.get('error_code') == 0:
        return resp.get('result')
    else:
        raise ValueError('数据聚合接口返回数据错误')


def save_story_db(date):
    try:
        storys = get_history_story_list(URL, date.tm_mon, date.tm_mday)
    except ValueError:
        return
    # 健壮性管理

    for result in storys:
        try:
            story_info = get_history_story_info(URL_INFO, int(result.get('e_id')))
        except ValueError:
            return
        story_info = story_info[0]
        story = HistoryStory.objects.get_or_create(
            e_id=int(result.get('e_id')),
            title=result.get('title'),
            date=result.get('date'),
            day=result.get('day'),
            content=story_info.get('content'),
            pic_no=story_info.get('picNo'),
        )
        if story[0].pic_no <=0:
            continue
        for pic_url in story_info.get('picUrl'):
            StoryPic.objects.create(
                story=story[0],
                pic_id=pic_url.get('id'),
                pic_url=pic_url.get('url'),
                pic_title=pic_url.get('pic_title'),
            )


if __name__ == '__main__':
    date = time.localtime(time.time())
    save_story_db(date)
