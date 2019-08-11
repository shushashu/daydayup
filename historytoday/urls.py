from django.conf.urls import url
from django.urls import path

from rest_framework import routers

import historytoday.views as views

router = routers.DefaultRouter()
router.register(r'hts', views.HistoryStoryViews, basename='hts')

urlpatterns = [
    path('info/<int:num>/', views.history_info, name='history_info'),
]

urlpatterns += router.urls
