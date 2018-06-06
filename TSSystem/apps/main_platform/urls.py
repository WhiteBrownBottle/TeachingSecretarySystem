#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import url

from . import views

app_name = 'main_platform'

urlpatterns = [

    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^modify/$', views.ModifyView.as_view(), name='Modify'),
    url(r'^student/', views.StudentView.as_view(), name='stuIndex'),


    url(r'^media/\w+/\d+\.\w+', views.fileDownloadView.as_view(), name='fileDownload')



]