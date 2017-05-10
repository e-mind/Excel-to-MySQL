from django.conf.urls import url, include
from apps.convertidor.views import bd
urlpatterns = [
    url(r'^$',bd, name='bd'),
    ]
