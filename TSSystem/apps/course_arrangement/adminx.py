#!/usr/bin/env python
# encoding: utf-8

import xadmin

from .models import Selection, Course


class SelectionAdmin(object):

    list_display = ['course_period', 'course_weekday', 'course_time', 'course_building', 'course_classroom', 'selection', 'is_empty']

    search_fields = ['course_period', 'course_weekday', 'course_time', 'course_building', 'course_classroom', 'selection', 'is_empty']

    list_filter = ['course_period', 'course_weekday', 'course_time', 'course_building', 'course_classroom', 'selection', 'is_empty']


class CourseAdmin(object):

    list_display = ['course_id', 'course_name', 'course_point', 'course_type', 'course_teacher', 'course_capacity', 'course_priority']

    search_fields = ['course_id', 'course_name', 'course_point', 'course_type', 'course_teacher', 'course_capacity', 'course_priority']

    list_filter = ['course_id', 'course_name', 'course_point', 'course_type', 'course_teacher', 'course_capacity', 'course_priority']


xadmin.site.register(Selection, SelectionAdmin)
xadmin.site.register(Course, CourseAdmin)