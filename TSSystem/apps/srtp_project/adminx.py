#!/usr/bin/env python
# encoding: utf-8

import xadmin
from .models import Project, Schedule

class ProjectAdmin(object):

    list_display = ['project_id', 'project_name', 'project_type', 'project_rank']

    search_fields = ['project_id', 'project_name', 'project_type', 'project_rank']

    list_filter = ['project_id', 'project_name', 'project_type', 'project_rank']


class ScheduleAdmin(object):

    list_display = ['schedule_date', 'schedule_num', 'schedule_detail']

    search_fields = ['schedule_date', 'schedule_num', 'schedule_detail']

    list_filter = ['schedule_date', 'schedule_num', 'schedule_detail']


xadmin.site.register(Project, ProjectAdmin)
xadmin.site.register(Schedule, ScheduleAdmin)
