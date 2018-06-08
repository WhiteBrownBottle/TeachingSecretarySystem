#!/usr/bin/env python
# encoding: utf-8
from django.contrib.auth.hashers import make_password, check_password


def session_judge(request):
    if 'user_id' in request.session and 'user_type' in request.session:
        user_type = request.session['user_type']
    else:
        del request.session
        return True
    if check_password('3', user_type):
        return False
    else:
        del request.session
        return True


def session_judge_teacher(request):
    if 'user_id' in request.session and 'user_type' in request.session:
        user_type = request.session['user_type']
    else:
        return True
    if check_password('2', user_type):
        return False
    else:
        return True