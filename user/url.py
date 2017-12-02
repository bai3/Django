from django.conf.urls import url
from user.views import *

urlpatterns = [
    url(r'^login$', login),
    url(r'^register$', register),
]