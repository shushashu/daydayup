from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.conf import settings

import json


@require_http_methods(['POST'])
def ci(request):
    print(request)
    if getattr(request, 'HTTP_X_USER_AGENT', None) == settings.GIT_USER_AGENT and \
            getattr(request, 'HTTP_X_GITHUB_EVENT', None) == settings.X_GIT_EVENT:
        return JsonResponse(json.loads(request.body))
    else:
        return JsonResponse(dict(msg='版本更新失败'))
