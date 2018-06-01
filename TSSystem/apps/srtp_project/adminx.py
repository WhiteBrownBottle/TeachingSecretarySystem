#!/usr/bin/env python
# encoding: utf-8

import xadmin
from .models import Project

class ProjectAdmin(object):

    list_display = ['project_id', 'project_name', 'project_type', 'project_rank']

    search_fields = ['project_id', 'project_name', 'project_type', 'project_rank']

    list_filter = ['project_id', 'project_name', 'project_type', 'project_rank']


xadmin.site.register(Project, ProjectAdmin)
