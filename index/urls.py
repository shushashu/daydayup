from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index_view, name='index'),
    url(r'^index/', views.index_view)
    # url(r'^test_ci', views.test_ci, name='ci'),
]
