#!/usr/bin/env python
# encoding: utf-8

import xadmin
from .models import Student, Teacher


class StudentAdmin(object):
    # 配置后台我们需要显示的列
    list_display = ['s_id', 's_name', 's_gender']
    # 配置搜索字段,不做时间搜索
    search_fields = ['s_id', 's_name', 's_gender']
    # 配置筛选字段
    list_filter = ['s_id', 's_name', 's_gender']

class TeacherAdmin(object):

    list_display = ['t_id', 't_name', 't_gender', 't_title']

    search_fields = ['t_id', 't_name', 't_gender', 't_title']

    list_filter = ['t_id', 't_name', 't_gender', 't_title']


xadmin.site.register(Student, StudentAdmin)
xadmin.site.register(Teacher, TeacherAdmin)




