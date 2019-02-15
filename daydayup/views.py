from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


@csrf_exempt
@require_http_methods(['POST'])
def ci(request):
    print(request)
    return JsonResponse(dict(msg='版本更新成功'))
