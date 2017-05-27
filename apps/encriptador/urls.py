from django.conf.urls import url, include
from apps.encriptador.views import entrada
urlpatterns = [
    url(r'^$',entrada, name='entrada'),
    ]
