#!/usr/bin/env python
# encoding: utf-8

import xadmin
from xadmin import views

from .models import Student


# X admin的全局配置信息设置
class BaseSetting(object):
    # 主题功能开启
    enable_themes = True
    use_bootswatch = True


class StudentAdmin(object):
    # 配置后台我们需要显示的列
    list_display = ['s_id', 's_name', 's_gender']
    # 配置搜索字段,不做时间搜索
    search_fields = ['s_id', 's_name', 's_gender']
    # 配置筛选字段
    list_filter = ['s_id', 's_name', 's_gender']


xadmin.site.register(Student, StudentAdmin)




