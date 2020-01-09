from django.conf.urls import url
from .views import get_bikes, forsale_bikes, bike_detail, create_or_edit_bike
from home.views import index

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^bikes/', get_bikes, name='get_bikes'),
    url(r'^sales/', forsale_bikes, name='forsale_bikes'),
    url(r'^(?P<pk>\d+)/$', bike_detail, name='bike_detail'),
    url(r'^new/$', create_or_edit_bike, name='new_bike'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_bike, name='edit_bike'),
]

