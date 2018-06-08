#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import url

from . import views

app_name = 'student'

urlpatterns = [

    url(r'^Info/$', views.stuInfoView.as_view(), name='Info'),

    url(r'^SrtpHome/$', views.stuSrtpHomeView.as_view(), name='Srtp_Home'),
    url(r'^SrtpProlist/$', views.stuSrtpProListView.as_view(), name='Srtp_Prolist'),
    url(r'^SrtpProManage/$', views.stuSrtpProManageView.as_view(), name='Srtp_ProManage'),
    url(r'^SrtpProApply/$', views.stuSrtpProApplyView.as_view(), name='Srtp_ProApply'),


    url(r'^SrtpProInfo/$', views.stuSrtpProInfoView.as_view(), name='Srtp_ProInfo'),
    url(r'^SrtpScheduleManage/$', views.stuSrtpScheduleManageView.as_view(), name='Srtp_ScheduleManage'),
    url(r'^SrtpFundManage/$', views.stuSrtpFundManageView.as_view(), name='Srtp_FundManage'),
    url(r'^SrtpResultManage/$', views.stuSrtpResultManageView.as_view(), name='Srtp_ResultManage'),
    url(r'^SrtpAddtionFunds/$', views.stuSrtpAddtionFundsView.as_view(), name='Srtp_AddtionFunds'),
    url(r'^SrtpMidTermApply/$', views.stuSrtpMidTermApplyView.as_view(), name='Srtp_MidTermApply'),
    url(r'^SrtpConcluApply/$', views.stuSrtpConcluApplyView.as_view(), name='Srtp_ConcluApply'),

    url(r'^SrtpNotification/(?P<notifi_id>\d+)/$', views.stuSrtpNotifiView.as_view(), name='Srtp_Notifi'),
    url(r'^SrtpSpecificInfo/(?P<project_id>\d+)/$', views.stuSrtpSpecificInfoView.as_view(), name='Srtp_SpecificInfo'),


    url(r'^GraHome/$', views.stuGraHomeView.as_view(), name='Gra_Home'),
    url(r'^GraNotification/(?P<notifi_id>\d+)/$', views.stuGraNotifiView.as_view(), name='Gra_Notifi'),
    url(r'^GraModelfile/$', views.stuGraModelfileView.as_view(), name='Gra_Modelfile'),
    url(r'^GraProposal/$', views.stuGraProposalView.as_view(), name='Gra_Proposal'),
    url(r'^GraMidterm/$', views.stuGraMidtermView.as_view(), name='Gra_Midterm' ),
    url(r'^GraPaper/$', views.stuGraPaperView.as_view(), name='Gra_Paper')

]