from django.conf.urls import url
from django.urls import include

from .views import (weixin_login, weixin_authorization, )

from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    url(r'^weixin_login/', weixin_login, name='weixin_login'),
    url(r'^weixin_authorization/', weixin_authorization, name='weixin_authorization'),
]
