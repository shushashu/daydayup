from django.shortcuts import render

# Create your views here.

from pfp import models


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
