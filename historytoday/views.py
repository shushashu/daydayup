from django.shortcuts import render
from django.http.response import Http404

import historytoday.models as story_models


# Create your views here.

def historylist_view(request):
    return render(request, 'index.html', locals())


def history_info(request, num):
    try:
        story_info = story_models.HistoryStory.objects.get(e_id=num)
    except Exception:
        return Http404
    return render(request, 'historytoday/story_info.html', locals())
