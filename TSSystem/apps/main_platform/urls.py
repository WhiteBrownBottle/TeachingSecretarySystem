#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'main_platform'

urlpatterns = [

    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^modify/$', views.ModifyView.as_view(), name='Modify'),
    url(r'^student/', views.StudentView.as_view(), name='stuIndex'),

    url(r'stuInfo/', views.stuInfoView.as_view(), name='stu_Info'),


    url(r'^stuSrtpHome/', views.stuSrtpHomeView.as_view(), name='stuSrtp_Home'),
    url(r'^stuSrtpProlist/', views.stuStrpProListView.as_view(), name='stuSrtp_Prolist'),
    url(r'^stuSrtpProManage/', views.stuStrpProManageView.as_view(), name='stuSrtp_ProManage'),
    url(r'^stuSrtpProApply/', views.stuSrtpProApplyView.as_view(), name='stuSrtp_ProApply'),


    url(r'^stuSrtpProInfo/', views.stuSrtpProInfoView.as_view(), name='stuSrtp_ProInfo'),
    url(r'^stuSrtpScheduleManage/', views.stuSrtpScheduleManageView.as_view(), name='stuSrtp_ScheduleManage'),
    url(r'^stuSrtpFundManage/', views.stuSrtpFundManageView.as_view(), name='stuSrtp_FundManage'),
    url(r'^stuSrtpResultManage/', views.stuSrtpResultManageView.as_view(), name='stuSrtp_ResultManage'),
    url(r'^stuSrtpAddtionFunds/', views.stuSrtpAddtionFundsView.as_view(), name='stuSrtp_AddtionFunds'),
    url(r'stuSrtpMidTermApply/', views.stuSrtpMidTermApplyView.as_view(), name='stuSrtp_MidTermApply'),
    url(r'stuSrtpConcluApply/', views.stuSrtpConcluApplyView.as_view(), name='stuSrtp_ConcluApply'),

    url(r'^media/\w+/\d+\.\w+', views.fileDownloadView.as_view(), name='fileDownload')

]