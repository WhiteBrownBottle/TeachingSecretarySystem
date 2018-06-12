#!/usr/bin/env python
# encoding: utf-8

from student.models import Student
from teacher.models import Teacher
from django.core.mail import send_mail
from django.conf import settings
from random import Random
from django.contrib.auth.hashers import check_password, make_password



# 生成随机字符串
def random_str(random_length=4):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(random_length):
        str += chars[random.randint(0, length)]
    return str


# 发送注册邮件
def send_forgetpwd_email(email, user_type, object):
    # 发送之间先保存到数据库，到时候查询链接是否存在

    # 实例化一个EmailVerifyRecord对象
    # 生成随机的code放入链接
    random_pwd = random_str(4)

    email_title = ""
    email_body = ""

    if user_type == '2':
        object.teacher_password = make_password(random_pwd)
        object.save()
        email_title = "找回密码(教师）——本科教学秘书辅助系统 "
        email_body = "您的密码已被格式化为{0}, 请登陆后自行修改".format(random_pwd)
        send_status = send_mail(email_title, email_body, settings.EMAIL_FROM, [email])

        if send_status:
            pass

    if user_type == '3':
        object.teacher_password = make_password(random_pwd)
        object.save()
        email_title = "找回密码(学生）——本科教学秘书辅助系统 "
        email_body = "您的密码已被格式化为%s, 请登陆后自行修改".format(random_pwd)
        send_status = send_mail(email_title, email_body, settings.EMAIL_FROM, [email])

        if send_status:
            pass
