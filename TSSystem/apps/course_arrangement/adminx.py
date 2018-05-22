#!/usr/bin/env python
# encoding: utf-8

import xadmin

from .models import Course, CourseTime


class CourseTimeAdmin(object):

    list_display = ['course_weekday', 'course_time']

    search_fields = ['course_weekday', 'course_time']

    list_filter = ['course_weekday', 'course_time']


class CourseAdmin(object):

    list_display = ['course_id', 'course_name', 'course_location', 'course_length']

    search_fields = ['course_id', 'course_name', 'course_location', 'course_length']

    list_filter = ['course_id', 'course_name', 'course_location', 'course_length']


xadmin.site.register(CourseTime, CourseTimeAdmin)
xadmin.site.register(Course, CourseAdmin)