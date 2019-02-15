from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

import json
import os, sys


@csrf_exempt
@require_http_methods(['POST'])
def ci(request):
    print(request)
    print(request.META.get('HTTP_USER_AGENT', None))
    if request.META.get('HTTP_USER_AGENT', None) == settings.GIT_USER_AGENT and \
            request.META.get('HTTP_X_GITHUB_EVENT', None) == settings.X_GIT_EVENT:
        body = json.loads(str(request.body))
        return JsonResponse(body)
    else:
        return JsonResponse(dict(msg='error'))
