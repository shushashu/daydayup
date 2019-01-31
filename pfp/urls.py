'''

:autor  heroHu
:time   2019/01/03
'''

from django.conf.urls import url

from pfp import views

urlpatterns = [
    url(r'^upload_csv/', view=views.upload_csv, name='upload'),
]