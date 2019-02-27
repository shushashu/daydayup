from django.shortcuts import render
from django.http.response import (HttpResponseNotFound, JsonResponse)
from django.views.decorators.csrf import csrf_exempt

from pfp.models import (quantitative_Investment, models as f_models)


# Create your views here.


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


@csrf_exempt
def insert_data_for_csv(request):
    '''
    使用csv 导入交易数据
    :param request:
    :return:
    '''

    if request.method == 'GET':
        return render(request, 'pfp/quantitative.html', locals())
    elif request.method == 'POST':
        files = request.FILES.lists()
        target = quantitative_Investment.Target.objects.all()
        transatic = quantitative_Investment.TargetTransaction.objects.all()
        for f in files:
            print(f)
    else:
        return render(request, HttpResponseNotFound)
