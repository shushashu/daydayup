from django.shortcuts import render

from daydayup import settings
from . import models


# Create your views here.

def index_view(request):
    print(settings.STATIC_ROOT, settings.STATIC_URL)
    return render(request, 'index.html', locals())
