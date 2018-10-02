from django.conf.urls import url
from app.app_views.highchart_view import *

urlpatterns = [
    url(r'^$', index, name='index'),
]