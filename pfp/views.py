from django.shortcuts import render
from django.http.response import HttpResponseNotFound

# Create your views here.

from pfp.models import (quantitative_Investment, models as f_models)


def upload_csv(request):
    '''
    上传用户账单流水
    :param request:
    :return:
    '''
    if request.method == 'GET':
        return render(request, 'index.html', locals())
    if request.method == 'POST':
        pass


def insert_data_for_csv(request):
    '''
    使用csv 导入交易数据
    :param request:
    :return:
    '''

    if request.method == 'GET':
        return render(request, 'quantitative.html', locals())
    elif request.method == 'POST':
        pass
    else:
        return render(request, HttpResponseNotFound)
