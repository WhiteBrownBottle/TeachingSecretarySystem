#!/usr/bin/env python
# encoding: utf-8

import xadmin
from .models import ModelFile, OpeningReport, MidtermReport, Dissertation


class ModelFileAdmin(object):

    list_display = ['file_name', 'file_url', 'file_date']

    search_fields= ['file_name', 'file_url', 'file_date']

    list_filter = ['file_name', 'file_url', 'file_date']


class OpeningReportAdmin(object):

    list_display = ['file_name', 'file_url', 'file_date', 'student_belong', 'teacher_to']

    search_fields = ['file_name', 'file_url', 'file_date', 'student_belong', 'teacher_to']

    list_filter = ['file_name', 'file_url', 'file_date', 'student_belong', 'teacher_to']


class MidtermReportAdmin(object):

    list_display = ['file_name', 'file_url', 'file_date', 'student_belong', 'teacher_to']

    search_fields = ['file_name', 'file_url', 'file_date', 'student_belong', 'teacher_to']

    list_filter = ['file_name', 'file_url', 'file_date', 'student_belong', 'teacher_to']


class DissertationAdmin(object):

    list_display = ['file_name', 'file_url', 'file_date', 'student_belong', 'teacher_to']

    search_fields = ['file_name', 'file_url', 'file_date', 'student_belong', 'teacher_to']

    list_filter = ['file_name', 'file_url', 'file_date', 'student_belong', 'teacher_to']


xadmin.site.register(ModelFile, ModelFileAdmin)
xadmin.site.register(OpeningReport, OpeningReportAdmin)
xadmin.site.register(MidtermReport, MidtermReportAdmin)
xadmin.site.register(Dissertation, DissertationAdmin)

