#!/usr/bin/env python
# encoding: utf-8
import xadmin
from .models import Teacher


class TeacherAdmin(object):

    list_display = ['teacher_id', 'teacher_name', 'teacher_gender', 'teacher_title']

    search_fields = ['teacher_id', 'teacher_name', 'teacher_gender', 'teacher_title']

    list_filter = ['teacher_id', 'teacher_name', 'teacher_gender', 'teacher_title']


xadmin.site.register(Teacher, TeacherAdmin)
