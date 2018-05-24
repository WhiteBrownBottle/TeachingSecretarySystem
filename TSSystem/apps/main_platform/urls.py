#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import url

from . import views

app_name = 'main_platform'

urlpatterns = [

    url(r'^$', views.IndexView.as_view(), name='index'),

]
