from django.conf.urls import url
from index.views import *
urlpatterns = [
    url(r'^index$', index),
    url(r'^article/(\w+)$', article),
    url(r'^articlesList$', allarticles),
    url(r'^show$', show),
]