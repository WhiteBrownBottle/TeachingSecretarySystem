#!/usr/bin/env python
# encoding: utf-8

import xadmin
from .models import Project, Schedule, Fund, Result, AddFund, MidTerm, Conclusion, Notification,NotifiFile

class ProjectAdmin(object):

    list_display = ['project_id', 'project_name', 'project_type', 'project_rank']

    search_fields = ['project_id', 'project_name', 'project_type', 'project_rank']

    list_filter = ['project_id', 'project_name', 'project_type', 'project_rank']


class ScheduleAdmin(object):

    list_display = ['schedule_date', 'schedule_num', 'schedule_detail']

    search_fields = ['schedule_date', 'schedule_num', 'schedule_detail']

    list_filter = ['schedule_date', 'schedule_num', 'schedule_detail']


class FundAdmin(object):

    list_display = ['fund_name', 'fund_type', 'fund_num', 'fund_date']

    search_fields = ['fund_name', 'fund_type', 'fund_num', 'fund_date']

    list_filter = ['fund_name', 'fund_type', 'fund_num', 'fund_date']


class ResultAdmin(object):

    list_display = ['result_name', 'result_type', 'result_date', 'result_master']

    search_fields = ['result_name', 'result_type', 'result_date', 'result_master']

    list_filter = ['result_name', 'result_type', 'result_date', 'result_master']


class AddFundAdmin(object):

    list_display = ['addfund_num', 'addfund_reason', 'addfund_check_status','project_belong']

    search_fields = ['addfund_num', 'addfund_reason', 'addfund_check_status', 'project_belong']

    list_filter = ['addfund_num', 'addfund_reason', 'addfund_check_status','project_belong']


class MidTermAdmin(object):

    list_display = ['midterm_file_name', 'midterm_deadline_date', 'midterm_check_status', 'midterm_check_point']

    search_fields = ['midterm_file_name', 'midterm_deadline_date', 'midterm_check_status', 'midterm_check_point']

    list_filter = ['midterm_file_name', 'midterm_deadline_date', 'midterm_check_status', 'midterm_check_point']


class ConclusionAdmin(object):

    list_display = ['conclusion_file_name', 'conclusion_deadline_date', 'conclusion_check_status', 'conclusion_check_point']

    search_fields = ['conclusion_file_name', 'conclusion_deadline_date', 'conclusion_check_status', 'conclusion_check_point']

    list_filter = ['conclusion_file_name', 'conclusion_deadline_date', 'conclusion_check_status', 'conclusion_check_point']


class NotificationAdmin(object):

    list_display = ['notifi_id', 'notifi_date', 'notifi_title', 'notifi_content']

    search_fields = ['notifi_id', 'notifi_date', 'notifi_title', 'notifi_content']

    list_filter = ['notifi_id', 'notifi_date', 'notifi_title', 'notifi_content']


class NotifiFileAdmin(object):

    list_display = ['notifi_belong', 'notifi_file_name', 'notifi_file_url']

    search_fields = ['notifi_belong', 'notifi_file_name', 'notifi_file_url']

    list_filter = ['notifi_belong', 'notifi_file_name', 'notifi_file_url']

xadmin.site.register(Project, ProjectAdmin)
xadmin.site.register(Schedule, ScheduleAdmin)
xadmin.site.register(Fund, FundAdmin)
xadmin.site.register(Result, ResultAdmin)
xadmin.site.register(AddFund, AddFundAdmin)
xadmin.site.register(MidTerm, MidTermAdmin)
xadmin.site.register(Conclusion, ConclusionAdmin)
xadmin.site.register(Notification, NotificationAdmin)
xadmin.site.register(NotifiFile, NotifiFileAdmin)
