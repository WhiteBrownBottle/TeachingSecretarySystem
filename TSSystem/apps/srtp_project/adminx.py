#!/usr/bin/env python
# encoding: utf-8

import xadmin
from .models import Project, Schedule, Fund, Result, AddFund

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


xadmin.site.register(Project, ProjectAdmin)
xadmin.site.register(Schedule, ScheduleAdmin)
xadmin.site.register(Fund, FundAdmin)
xadmin.site.register(Result, ResultAdmin)
xadmin.site.register(AddFund, AddFundAdmin)
