from django.shortcuts import render
from django.views import View
from users.models import Teacher, Student
from srtp_project.models import Project, Schedule
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
import django.utils.timezone as timezone
import time, datetime



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


class stuInfoView(View):

    def get(self, request):
        user_id = request.session['user_id']
        user_type = request.session['user_type']
        if str(user_type) != '3':
            del request.session
            return render(request, 'index.html')
        else:
            student = Student.objects.get(student_id=user_id)
            return render(request, 'personInfo/stuInfo.html', context={'student': student})

    def post(self, request):
        pass


class stuSrtpHomeView(View):

    def get(self, request):
        user_type = request.session['user_type']
        print(user_type)
        user_id =request.session['user_id']
        print(user_id)
        return render(request, 'stuSrtp/stuSrtpHome.html')

    def post(self, request):
        pass


class stuStrpProListView(View):

    def get(self, request):

        return render(request, 'stuSrtp/stuSrtpProList.html')

    def post(self, request):
        pass



class stuStrpProManageView(View):

    def get(self, request):
        return render(request, 'stuSrtp/stuSrtpProManage.html')

    def post(self, request):
        pass


class stuSrtpProApplyView(View):

    def get(self, request):
        return render(request, 'stuSrtp/stuSrtpProApply.html')


    def post(self, request):
        pass


class stuSrtpProInfoView(View):

    def get(self, request):
        user_id = request.session['user_id']
        user_type = request.session['user_type']
        if str(user_type) != '3':
            del request.session
            return render(request, 'index.html')
        else:
            student = Student.objects.get(student_id = user_id)
            srtp_project = Project.objects.get(project_appli_student_id = student.id)
            teacher_uid = srtp_project.project_teacher_id
            teacher = Teacher.objects.get(id = teacher_uid)
            teacher_name = teacher.teacher_name
            print(srtp_project)
            return render(request, 'stuSrtp/stuSrtpProInfo.html', context={'srtp_project': srtp_project,
                                                                           'student': student,
                                                                           'teacher_name': teacher_name})

    def post(self, request):
        pass


class stuSrtpScheduleManageView(View):

    def get(self, request):
        user_id = request.session['user_id']
        user_type = request.session['user_type']
        if str(user_type) != '3':
            del request.session
            return render(request, 'index.html')
        else:
            student = Student.objects.get(student_id=user_id)
            srtp_project = Project.objects.get(project_appli_student_id=student.id)
            schedule_list = Schedule.objects.filter(project_belong_id = srtp_project.project_id).order_by('schedule_date')
            print(schedule_list)
            return render(request, 'stuSrtp/stuSrtpScheduleManage.html', context={'schedule_list': schedule_list})

    def post(self, request):
        user_id = request.session['user_id']
        user_type = request.session['user_type']
        if str(user_type) != '3':
            del request.session
            return render(request, 'index.html')
        else:
            schedule_time = request.POST.get('time', datetime.datetime.now().strftime("%Y-%m-%d"))
            if schedule_time != '':
                schedule_date = datetime.datetime.strptime(schedule_time, "%Y-%m-%d %H:%M:%S").date()

            schedule_num = request.POST.get('select', '')
            schedule_detail = request.POST.get('jinzhan', '')

            student = Student.objects.get(student_id=user_id)
            srtp_project = Project.objects.get(project_appli_student_id=student.id)
            schedule = Schedule()
            schedule.schedule_date = schedule_date
            schedule.schedule_num = schedule_num
            schedule.schedule_detail = schedule_detail
            schedule.project_belong = srtp_project
            schedule.save()
            return HttpResponse('{"status": "success", "msg": "添加成功"}', content_type='application/json')







        pass

class stuSrtpFundManageView(View):

    def get(self, request):
        return render(request, 'stuSrtp/stuSrtpFundManage.html')

    def post(self, request):
        pass


class stuSrtpResultManageView(View):

    def get(self, request):
        return render(request, 'stuSrtp/stuSrtpResultManage.html')

    def post(self, request):
        pass


class stuSrtpAddtionFundsView(View):

    def get(self, request):
        return render(request, 'stuSrtp/stuSrtpAddtionFunds.html')

    def post(self, request):
        pass


class stuSrtpMidTermApplyView(View):

    def get(self, request):
        return render(request, 'stuSrtp/stuSrtpMidTermApply.html')

    def post(self, request):
        pass


class stuSrtpConcluApplyView(View):

    def get(self, request):
        return render(request, 'stuSrtp/stuSrtpConcluApply.html')

    def post(self, request):
        pass













