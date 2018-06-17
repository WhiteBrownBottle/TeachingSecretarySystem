#!/usr/bin/env python
# encoding: utf-8

import xadmin

from .models import Selection, Course


class SelectionAdmin(object):

    list_display = ['course_period', 'course_weekday', 'course_time', 'course_building', 'course_classroom', 'selection', 'is_empty', 'capacity']

    search_fields = ['course_period', 'course_weekday', 'course_time', 'course_building', 'course_classroom', 'selection', 'is_empty', 'capacity']

    list_filter = ['course_period', 'course_weekday', 'course_time', 'course_building', 'course_classroom', 'selection', 'is_empty', 'capacity']


class CourseAdmin(object):

    list_display = ['course_id', 'course_name', 'course_point', 'course_type', 'course_teacher', 'course_capacity', 'course_priority', 'is_arranged']

    search_fields = ['course_id', 'course_name', 'course_point', 'course_type', 'course_teacher', 'course_capacity', 'course_priority', 'is_arranged']

    list_filter = ['course_id', 'course_name', 'course_point', 'course_type', 'course_teacher', 'course_capacity', 'course_priority', 'is_arranged']


xadmin.site.register(Selection, SelectionAdmin)
xadmin.site.register(Course, CourseAdmin)