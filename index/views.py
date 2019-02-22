import time
from django.shortcuts import render
from django.conf import settings
from historytoday import models as history_models


def index_view(request):
    context_exct = {}
    today = time.gmtime()
    history_list = history_models.HistoryStory.objects.all().filter(day='%s/%s' % (today.tm_mon, today.tm_mday))
    return render(request, 'index.html', locals())
