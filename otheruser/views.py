from django.shortcuts import render
from django.conf import settings
from rest_framework.decorators import (api_view, permission_classes, authentication_classes)
from rest_framework.response import Response
from rest_framework import (status, permissions, authentication)

from weixin.client import WeixinAPI
from weixin.oauth2 import OAuth2AuthExchangeError


# Create your views here.

@permission_classes((permissions.AllowAny,))
@api_view(['GET'])
def weixin_authorization(request):
    code = request.GET.get('code')
    api = WeixinAPI(
        appid=settings.APP_ID,
        app_secret=settings.APP_SECRERT,
        redirect_uri=settings.REDIRECT_URI
    )

    auth_info = api.exchange_code_for_access_token(code=code)
    api = WeixinAPI(access_token=auth_info['access_token'])
    resp = api.user(openid=auth_info['openid'])
    return Response(data=resp, status=status.HTTP_200_OK)


@permission_classes((permissions.AllowAny,))
@api_view(['GET'])
def weixin_login(request):
    api = WeixinAPI(
        appid=settings.APP_ID,
        app_secret=settings.APP_SECRERT,
        redirect_uri=settings.REDIRECT_URI
    )
    redirect_uri = api.get_authorize_login_url(scope=('snsapi_login',))
    return Response(data=redirect_uri, status=status.HTTP_200_OK)
