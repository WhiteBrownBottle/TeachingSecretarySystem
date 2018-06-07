from django.shortcuts import render
from django.views import View
from student.models import Student
from teacher.models import Teacher
from srtp_project.models import Project, Schedule, Fund, Result, AddFund, MidTerm, Conclusion, NotifiFile
from utils.session_judge import session_judge, session_judge_teacher
from utils.file_utils import file_iterator, file_upload
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password, make_password
import django.utils.timezone as timezone
import time, datetime, os
from django.db.models import Q
from django.conf import settings
from django.http import StreamingHttpResponse



# Create your views here.


class IndexView(View):
    """
    首页
    """
    def get(self, request):

        return render(request, 'index.html',)


class LoginView(View):
    """
    登陆
    """
    def get(self, request):
        return render(request, 'index.html',)


    def post(self,request):
        user_type = request.POST.get('identify', '')
        user_name = request.POST.get('username', '')
        user_password = request.POST.get('password', '')
        if user_type == '1':
            # 管理员身份
            admin_user = authenticate(username=user_name, password=user_password)
            if admin_user is not None:
                login(request, admin_user)
                return HttpResponse('{"status": "success", "msg": %s}' % (user_type), content_type='application/json')
            else:
                return HttpResponse('{"status": "fail", "msg": "信息错误，用户不存在"}', content_type='application/json')
        elif user_type == '2':
            # 教师身份
            teacher_user = Teacher.objects.get(teacher_id = int(user_name))
            if teacher_user is not None:
                if check_password(user_password, teacher_user.teacher_password):
                    request.session['user_type'] = user_type
                    request.session['user_id'] = teacher_user.teacher_id
                    return HttpResponse('{"status": "success", "msg": %s}' %(user_type),
                                        content_type='application/json')
                else:
                    return HttpResponse('{"status": "fail", "msg": "密码错误"}', content_type='application/json')
            else:
                return HttpResponse('{"status": "fail", "msg": "信息错误，用户不存在"}', content_type='application/json')

        elif user_type == '3':
            #学生身份
            student_user = Student.objects.get(student_id = int(user_name))
            if student_user is not None:
                if check_password(user_password, student_user.student_password):
                    request.session['user_type'] = user_type
                    request.session['user_id'] = student_user.student_id
                    return HttpResponse('{"status": "success", "msg": %s}' % (user_type),
                                        content_type='application/json')
                else:
                    return HttpResponse('{"status": "fail", "msg": "密码错误"}', content_type='application/json')
            else:
                return HttpResponse('{"status": "fail", "msg": "输入错误，用户不存在"}', content_type='application/json')


class LogoutView(View):
    """
    登出
    """
    def get(self, request):
        del request.session['user_id']
        del request.session['user_type']
        return HttpResponseRedirect('/')






class ModifyView(View):

    def get(self, request):
        return render(request, 'personInfo/modify.html')

    def post(self, request):
        if 'user_id' in request.session and 'user_type' in request.session:
            user_type = request.session['user_type']
            user_id = request.session['user_id']
        else:
            del request.session
            return HttpResponse('{"status": "fail", "msg": "身份错误"}', content_type='application/json')
        if str(user_type) == '2':
            try:
                teacher = Teacher.objects.get(teacher_id=user_id)
            except Teacher.DoesNotExist:
                return HttpResponse('{"status": "fail", "msg": "用户不存在"}', content_type='application/json')
            old_pass = request.POST.get('oldpass', '')
            new_pass = request.POST.get('newpass', '')
            if check_password(old_pass, teacher.teacher_password):
                teacher.teacher_password = make_password(new_pass)
                teacher.save()
                return HttpResponse('{"status": "success", "msg": "修改成功", "user_type": %s}' % (user_type), content_type='application/json')
            else:
                return HttpResponse('{"status": "fail", "msg": "原密码不匹配"}', content_type='application/json')
        elif str(user_type) == '3':
            try:
                student = Student.objects.get(student_id=user_id)
            except Teacher.DoesNotExist:
                return HttpResponse('{"status": "fail", "msg": "用户不存在"}', content_type='application/json')
            old_pass = request.POST.get('oldpass', '')
            new_pass = request.POST.get('newpass', '')
            if check_password(old_pass, student.student_password):
                student.student_password = make_password(new_pass)
                student.save()
                return HttpResponse('{"status": "success", "msg": "修改成功", "user_type": %s}' %(user_type), content_type='application/json')
            else:
                return HttpResponse('{"status": "fail", "msg": "原密码不匹配"}', content_type='application/json')

        else:
            del request.session
            return render(request, 'index.html', )


class StudentView(View):

    def get(self, request):
        return render(request, 'stuIndex.html',)

    def post(self, request):
        return render(request, 'stuIndex.html',)


class TeacherView(View):

    def get(self, request):
        return render(request, 'teaIndex.html',)

    def post(self, request):
        return render(request, 'teaIndex.html',)


class fileDownloadView(View):

    def get(self, request):
            url = str(request.get_full_path())
            file_url = url.split('/')
            file_name = '未知错误'
            if file_url[2] == 'SrtpResult':
                file = Result.objects.get(result_file_url = url)
                file_name = file.result_file_name
            elif file_url[2] == 'SrtpAppli':
                file = Project.objects.get(project_appli_url = url)
                file_name = file.project_appli_name
            elif file_url[2] == 'SrtpMidTerm':
                file = MidTerm.objects.get(midterm_file_url=url)
                file_name = file.midterm_file_name
            elif file_url[2] == 'SrtpConclusion':
                file = Conclusion.objects.get(conclusion_file_url=url)
                file_name = file.conclusion_file_name
            elif file_url[2] == 'SrtpNotification':
                url_list = url.split('/')
                special_url = url_list[2] + '/' + url_list[3]
                file = NotifiFile.objects.get(notifi_file_url = special_url)
                file_name = file.notifi_file_name
            the_file_name = settings.MEDIA_ROOT + '/' + file_url[2] + '/' + file_url[3]
            response = StreamingHttpResponse(file_iterator(the_file_name))
            response['Content-Type'] = 'application/octet-stream'
            response['Content-Disposition'] = 'attachment; filename=%s' % str(file_name).encode(
                'utf-8').decode('ISO-8859-1')
            return response


    def post(self, request):
        pass













