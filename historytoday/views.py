from django.shortcuts import render
from django.http.response import Http404
from django.views.generic import TemplateView

from rest_framework import decorators, response, status, permissions, authentication, viewsets

import historytoday.models.models as story_models
from historytoday.models import serializers as hts_serializers


# Create your views here.

def historylist_view(request):
    return render(request, 'index.html', locals())


def history_info(request, num):
    try:
        story_info = story_models.HistoryStory.objects.get(e_id=num)
    except Exception:
        return Http404
    return render(request, 'historytoday/story_info.html', locals())


class HistoryStoryViews(viewsets.ModelViewSet):
    serializer_class = hts_serializers.HistoryStorySerializer
    queryset = story_models.HistoryStory.objects.all()
    permission_classes = permissions.AllowAny,
    http_method_names = ['get', 'post']
