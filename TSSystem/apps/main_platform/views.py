from django.shortcuts import render
from django.views import View
from student.models import Student
from teacher.models import Teacher
from srtp_project.models import Project, Schedule, Fund, Result, AddFund, MidTerm, Conclusion
from utils.session_judge import session_judge
from utils.file_utils import file_iterator, file_upload
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
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


class ModifyView(View):

    def get(self, request):
        return render(request, 'personInfo/modify.html')

    def post(self, request):
        pass


class StudentView(View):

    def get(self, request):
        return render(request, 'stuIndex.html',)

    def post(self, request):
        return render(request, 'stuIndex.html',)

class fileDownloadView(View):

    def get(self, request):
        if session_judge(request):
            return render(request, 'index.html')
        else:

            url = str(request.get_full_path())
            file_url = url.split('/')
            file_name = '未知错误'
            if file_url[2] == 'SrtpResult':
                file = Result.objects.get(result_file_url = url)
                file_name = file.result_file_name
            elif file_url[2] == 'SrtpAppli':
                file = Project.objects.get(project_appli_url = url)
                file_name = file.project_appli_name
            the_file_name = settings.MEDIA_ROOT + '/' + file_url[2] + '/' + file_url[3]
            response = StreamingHttpResponse(file_iterator(the_file_name))
            response['Content-Type'] = 'application/octet-stream'
            response['Content-Disposition'] = 'attachment; filename=%s' % str(file_name).encode(
                'utf-8').decode('ISO-8859-1')
            return response


    def post(self, request):
        pass













