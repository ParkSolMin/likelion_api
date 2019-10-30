from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
import melong.views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('', melong.views.melong, name='melong'),
    path('/marker', melong.views.marker, name='marker'),
]