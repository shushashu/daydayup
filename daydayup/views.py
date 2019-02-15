from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

import json
import os, sys


@csrf_exempt
@require_http_methods(['POST'])
def ci(request):
    if request.META.get('HTTP_USER_AGENT', None) == settings.GIT_USER_AGENT and \
            request.META.get('HTTP_X_GITHUB_EVENT', None) == settings.X_GIT_EVENT:
        body = json.loads(request.body.decode(encoding='utf8'))
        # 检查是否满足版本更新条件
        os.system('sh /%s/git_update.sh %s %s %s' % (
            os.path.dirname(settings.BASE_DIR),
            os.path.dirname(settings.BASE_DIR),
            settings.BASE_DIR,
            os.environ.get('VIRTUAL_ENV'),))
        return JsonResponse(dict(msg='succeed'))
    else:
        return JsonResponse(dict(msg='error'))
