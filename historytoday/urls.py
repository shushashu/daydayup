from django.conf.urls import url
from django.urls import path

import historytoday.views as views

urlpatterns = [
    url(r'^historylist', views.historylist_view, name='history_list'),
    path('info/<int:num>/', views.history_info, name='history_info'),
]
