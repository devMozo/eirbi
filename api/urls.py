from django.conf.urls import url
from views import *
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$',index, name='api'),
    url(r'^propiedad/(?P<propiedadid>\d+)$', propiedad, name="propiedad"),
    url(r'^reservaPropiedad/', reservaPropiedad, name='reservaPropiedad'),
    url(r'^reservaPropiedad/([0-9]+)/$', reservaExitosa, name='reservaExitosa'),
]

