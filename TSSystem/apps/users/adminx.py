#!/usr/bin/env python
# encoding: utf-8

import xadmin
from .models import Student, Teacher


class StudentAdmin(object):
    # 配置后台我们需要显示的列
    list_display = ['student_id', 'student_name', 'student_gender']
    # 配置搜索字段,不做时间搜索
    search_fields = ['student_id', 'student_name', 'student_gender']
    # 配置筛选字段
    list_filter = ['student_id', 'student_name', 'student_gender']

class TeacherAdmin(object):

    list_display = ['teacher_id', 'teacher_name', 'teacher_gender', 'teacher_title']

    search_fields = ['teacher_id', 'teacher_name', 'teacher_gender', 'teacher_title']

    list_filter = ['teacher_id', 'teacher_name', 'teacher_gender', 'teacher_title']


xadmin.site.register(Student, StudentAdmin)
xadmin.site.register(Teacher, TeacherAdmin)




