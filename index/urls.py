
from django.conf.urls import url

import index.models as mo
import index.views as views

urlpatterns = [
    url(r'', views.index_views)
 ]