#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import url
from . import views

app_name = 'teacher'

urlpatterns = [
    url(r'^SrtpHome/', views.teaSrtpHomeView.as_view(), name='Srtp_Home'),
    url(r'^Info/', views.teaInfoView.as_view(), name='Info'),
    url(r'^SrtpProlist/', views.teaSrtpProListView.as_view(), name='Srtp_Prolist'),
    url(r'^SrtpProManage/(?P<project_id>\d+)/$', views.teaSrtpProManageView.as_view(), name='Srtp_ProManage'),


    url(r'^SrtpProInfo/(?P<project_id>\d+)/$', views.teaSrtpProInfoView.as_view(), name='Srtp_ProInfo'),
    url(r'^SrtpScheduleManage/(?P<project_id>\d+)/$', views.teaSrtpScheduleManageView.as_view(), name='Srtp_ScheduleManage'),
    url(r'^SrtpFundManage/(?P<project_id>\d+)/$', views.teaSrtpFundManageView.as_view(), name='Srtp_FundManage'),
    url(r'^SrtpResultManage/(?P<project_id>\d+)/$', views.teaSrtpResultManageView.as_view(), name='Srtp_ResultManage'),
    url(r'^SrtpAddtionFunds/(?P<project_id>\d+)/$', views.teaSrtpAddtionFundsView.as_view(), name='Srtp_AddtionFunds'),
    url(r'^SrtpMidTermApply/(?P<project_id>\d+)/$', views.teaSrtpMidTermApplyView.as_view(), name='Srtp_MidTermApply'),
    url(r'^SrtpConcluApply/(?P<project_id>\d+)/$', views.teaSrtpConcluApplyView.as_view(), name='Srtp_ConcluApply'),
    url(r'^SrtpProPublish/', views.teaSrtpProPublishView.as_view(), name='Srtp_ProPublish'),
    url(r'^SrtpNotification/(?P<notifi_id>\d+)/$', views.teaSrtpNotifiView.as_view(), name='Srtp_Notifi'),
    url(r'^SrtpSpecificInfo/(?P<project_id>\d+)/$', views.teaSrtpSpecificInfoView.as_view(), name='Srtp_SpecificInfo'),


    url(r'^GraHome/$', views.teaGraHomeView.as_view(), name='Gra_Home'),
    url(r'^GraNotification/(?P<notifi_id>\d+)/$', views.teaGraNotifiView.as_view(), name='Gra_Notifi'),
    url(r'^GraModelfile/$', views.teaGraModelfileView.as_view(), name='Gra_Modelfile'),
    url(r'^GraProposal/$', views.teaGraProposalView.as_view(), name='Gra_Proposal'),
    url(r'^GraMidterm/$', views.teaGraMidtermView.as_view(), name='Gra_Midterm' ),
    url(r'^GraPaper/$', views.teaGraPaperView.as_view(), name='Gra_Paper'),

]