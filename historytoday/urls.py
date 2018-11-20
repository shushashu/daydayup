from django.conf.urls import url

import historytoday.views as views

urlpatterns = [
    url(r'historylist', views.historylist_view, name='history_list'),
]
