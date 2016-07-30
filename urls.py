from django.conf.urls import include, url
from views import *

urlpatterns = [
    url(r'^districts_for_country/$', districts_for_country, name='districts_for_country'),
]
