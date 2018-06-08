#!/usr/bin/env python
# encoding: utf-8

import xadmin
from xadmin import views
from .models import Class, Grade, Notification, NotifiFile


# X admin的全局配置信息设置

class GlobalSetting(object):
    site_title = '本科教务秘书辅助系统'   #设置头标题
    site_footer = 'USTBTSS'  #设置脚标题
    menu_style = 'accordion'


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

class ClassAdmin(object):
    # 配置后台我们需要显示的列
    list_display = ['class_name', 'grade_belong']

    search_fields = ['class_name', 'grade_belong']

    list_filter = ['class_name', 'grade_belong']


class GradeAdmin(object):

    list_display = ['grade_name']

    search_fields = ['grade_name']

    list_filter = ['grade_name']

class NotificationAdmin(object):

    list_display = ['notifi_id', 'notifi_date', 'notifi_title', 'notifi_content']

    search_fields = ['notifi_id', 'notifi_date', 'notifi_title', 'notifi_content']

    list_filter = ['notifi_id', 'notifi_date', 'notifi_title', 'notifi_content']


class NotifiFileAdmin(object):

    list_display = ['notifi_belong', 'notifi_file_name', 'notifi_file_url']

    search_fields = ['notifi_belong', 'notifi_file_name', 'notifi_file_url']

    list_filter = ['notifi_belong', 'notifi_file_name', 'notifi_file_url']



xadmin.site.register(Class, ClassAdmin)
xadmin.site.register(Grade, GradeAdmin)
xadmin.site.register(Notification, NotificationAdmin)
xadmin.site.register(NotifiFile, NotifiFileAdmin)
xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(views.BaseAdminView, BaseSetting)



