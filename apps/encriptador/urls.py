from django.conf.urls import url, include
from apps.encriptador.views import entrada, salida
urlpatterns = [
    url(r'^$',entrada, name='entrada'),
    url(r'^salida/$',salida, name='salida'),
    ]
