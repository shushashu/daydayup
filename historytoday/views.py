from django.shortcuts import render

import historytoday.models as mo


# Create your views here.

def historylist_view(request):
    return render(request, 'index.html', locals())
