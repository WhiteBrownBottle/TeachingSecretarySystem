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

    url(r'^EduReformHome/$', views.eduReformHomeView.as_view(), name='EduReform_home'),
    url(r'^EduReformApply/$', views.eduReformApplyView.as_view(), name='EduReform_Apply'),
    url(r'^EduReformManage/(?P<eduproject_id>\d+)/$', views.eduReformManageView.as_view(), name='EduReform_Manage'),

    url(r'^EduReformInfo/(?P<eduproject_id>\d+)/$', views.eduReformInfoView.as_view(), name='EduReform_Info'),
    url(r'^EduReformMidTermApply/(?P<eduproject_id>\d+)/$', views.eduReformMidTermApplyView.as_view(), name='EduReform_MidTermApply'),
    url(r'^EduReformConcluApply/(?P<eduproject_id>\d+)/$', views.eduReformConcluApplyView.as_view(), name='EduReform_ConcluApply'),
    url(r'^EduReformFundManage/(?P<eduproject_id>\d+)/$', views.eduReformFundManageView.as_view(), name='EduReform_FundManage'),
    url(r'^EduReformResultManage/(?P<eduproject_id>\d+)/$', views.eduReformResultManageView.as_view(), name='EduReform_ResultManage')

]