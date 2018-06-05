from django.shortcuts import render
from django.views import View
from users.models import Teacher, Student
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


class stuInfoView(View):

    def get(self, request):
        if session_judge(request):
            return HttpResponse('{"status": "fail", "msg": "/"}', content_type='application/json')
        else:
            student = Student.objects.get(student_id=request.session['user_id'])
            return render(request, 'personInfo/stuInfo.html', context={'student': student})

    def post(self, request):
        pass


class stuSrtpHomeView(View):

    def get(self, request):
        if session_judge(request):
            return HttpResponse('{"status": "fail", "msg": "/"}', content_type='application/json')
        else:
            return render(request, 'stuSrtp/stuSrtpHome.html')

    def post(self, request):
        pass


class stuStrpProListView(View):

    def get(self, request):

        return render(request, 'stuSrtp/stuSrtpProList.html')

    def post(self, request):
        pass



class stuSrtpProManageView(View):

    def get(self, request):
        if session_judge(request):
            return HttpResponse('{"status": "fail", "msg": "/"}', content_type='application/json')
        else:
            user_id = request.session['user_id']
            student = Student.objects.get(student_id=user_id)
            srtp_project = Project.objects.get(project_appli_student_id=student.id)
            addfund_checkok_list = AddFund.objects.filter(Q(project_belong_id = srtp_project.project_id)&Q(addfund_check_status = '1')&Q(addfund_add_status = '0'))
            if addfund_checkok_list != '':
                for addfund_checkok in addfund_checkok_list:
                    addfund_checkok_money = addfund_checkok.addfund_num
                    srtp_project.project_fund_approv += addfund_checkok_money
                    addfund_checkok.addfund_add_status = '1'
                    addfund_checkok.save()
            srtp_project.save()
            return render(request, 'stuSrtp/stuSrtpProManage.html')

    def post(self, request):
        if session_judge(request):
            return HttpResponse('{"status": "fail", "msg": "/"}', content_type='application/json')
        else:
            return HttpResponse('{"status": "success", "msg": "success"}', content_type='application/json')


class stuSrtpProApplyView(View):

    def get(self, request):
        if session_judge(request):
            return HttpResponse('{"status": "fail", "msg": "/"}', content_type='application/json')
        else:
            return render(request, 'stuSrtp/stuSrtpProApply.html')


    def post(self, request):
        if session_judge(request):
            return HttpResponse('{"status": "fail", "msg": "/"}', content_type='application/json')
        else:
            pass



class stuSrtpProInfoView(View):

    def get(self, request):
        if session_judge(request):
            return HttpResponse('{"status": "fail", "msg": "/"}', content_type='application/json')
        else:
            student = Student.objects.get(student_id = request.session['user_id'])
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
        if session_judge(request):
            return HttpResponse('{"status": "fail", "msg": "/"}', content_type='application/json')
        else:
            student = Student.objects.get(student_id=request.session['user_id'])
            srtp_project = Project.objects.get(project_appli_student_id=student.id)
            schedule_list = Schedule.objects.filter(project_belong_id = srtp_project.project_id).order_by('schedule_date')
            return render(request, 'stuSrtp/stuSrtpScheduleManage.html', context={'schedule_list': schedule_list})

    def post(self, request):
        if session_judge(request):
            return HttpResponse('{"status": "fail", "msg": "/"}', content_type='application/json')
        else:
            schedule_time = request.POST.get('time', datetime.datetime.now().strftime("%Y-%m-%d"))
            if schedule_time != '':
                schedule_date = datetime.datetime.strptime(schedule_time, "%Y-%m-%d %H:%M:%S").date()

            schedule_num = request.POST.get('select', '')
            schedule_detail = request.POST.get('jinzhan', '')

            student = Student.objects.get(student_id=request.session['user_id'])
            srtp_project = Project.objects.get(project_appli_student_id=student.id)
            schedule = Schedule()
            schedule.schedule_date = schedule_date
            schedule.schedule_num = schedule_num
            schedule.schedule_detail = schedule_detail
            schedule.project_belong = srtp_project
            schedule.save()
            return HttpResponse('{"status": "success", "msg": "添加成功"}', content_type='application/json')


class stuSrtpFundManageView(View):

    def get(self, request):
        if session_judge(request):
            return HttpResponse('{"status": "fail", "msg": "/"}', content_type='application/json')
        else:
            student = Student.objects.get(student_id=request.session['user_id'])
            srtp_project = Project.objects.get(project_appli_student_id=student.id)
            fund_list = Fund.objects.filter(project_belong_id = srtp_project.project_id).order_by('fund_date')
            return render(request, 'stuSrtp/stuSrtpFundManage.html', context={'fund_list': fund_list})

    def post(self, request):
        if session_judge(request):
            return HttpResponse('{"status": "fail", "msg": "/"}', content_type='application/json')
        else:
            fund_time = request.POST.get('riqi', datetime.datetime.now().strftime("%Y-%m-%d"))
            if fund_time != '':
                fund_date = datetime.datetime.strptime(fund_time, "%Y-%m-%d").date()
            fund_name = request.POST.get('jutizhichu', '')
            fund_type = request.POST.get('leibie', '12')
            fund_num = int(request.POST.get('jine', ''))
            student = Student.objects.get(student_id=request.session['user_id'])
            srtp_project = Project.objects.get(project_appli_student_id=student.id)
            fund = Fund()
            fund.fund_name = fund_name
            fund.fund_type = fund_type
            fund.fund_num = fund_num
            fund.fund_date = fund_date
            fund.project_belong = srtp_project
            fund.save()
            return HttpResponse('{"status": "success", "msg": "添加成功"}', content_type='application/json')



class stuSrtpResultManageView(View):

    def get(self, request):
        if session_judge(request):
            return HttpResponse('{"status": "fail", "msg": "/"}', content_type='application/json')
        else:
            user_id = request.session['user_id']
            student = Student.objects.get(student_id=user_id)
            srtp_project = Project.objects.get(project_appli_student_id=student.id)
            result_list = Result.objects.filter(project_belong_id=srtp_project.project_id).order_by('result_date')
            return render(request, 'stuSrtp/stuSrtpResultManage.html', context={'result_list': result_list})

    def post(self, request):
        if session_judge(request):
            return HttpResponse('{"status": "fail", "msg": "/"}', content_type='application/json')
        else:
            result_name = request.POST.get('mingcheng' '')
            result_type = request.POST.get('leixing', '7')
            result_date = request.POST.get('riqi', datetime.datetime.now().strftime("%Y-%m-%d"))
            if result_date != '':
                result_date = datetime.datetime.strptime(result_date, '%Y-%m-%d').date()
            result_master = request.POST.get('suoyouren', '')
            result_file = request.FILES.get('file')
            file_detail = file_upload(result_file, 'SrtpResult')
            student = Student.objects.get(student_id=request.session['user_id'])
            srtp_project = Project.objects.get(project_appli_student_id=student.id)
            result = Result()
            result.result_name = result_name
            result.result_type = result_type
            result.result_date = result_date
            result.result_master = result_master
            result.result_file_name = file_detail[0]
            result.result_file_url = file_detail[1]
            result.project_belong = srtp_project
            result.save()
            return HttpResponse('{"status": "success", "msg": "添加成功"}', content_type='application/json')



class stuSrtpAddtionFundsView(View):

    def get(self, request):
        if session_judge(request):
            return render(request, 'index.html')
        else:
            user_id = request.session['user_id']
            student = Student.objects.get(student_id=user_id)
            srtp_project = Project.objects.get(project_appli_student_id=student.id)
            addfund_list = AddFund.objects.filter(project_belong_id = srtp_project.project_id).order_by('addfund_date')
            return render(request, 'stuSrtp/stuSrtpAddtionFunds.html', context={'addfund_list': addfund_list})

    def post(self, request):
        if session_judge(request):
            return render(request, 'index.html')
        else:
            user_id = request.session['user_id']
            student = Student.objects.get(student_id=user_id)
            srtp_project = Project.objects.get(project_appli_student_id=student.id)
            addfund_num = request.POST.get('fund', '0')
            addfund_reason = request.POST.get('addReason', '')
            addfund = AddFund()
            addfund.addfund_num = int(addfund_num)
            addfund.addfund_reason = addfund_reason
            addfund.project_belong = srtp_project
            addfund.save()
            return HttpResponse('{"status": "success", "msg": "添加成功"}', content_type='application/json')


class stuSrtpMidTermApplyView(View):

    def get(self, request):
        if session_judge(request):
            return render(request, 'index.html')
        else:
            user_id = request.session['user_id']
            student = Student.objects.get(student_id=user_id)
            srtp_project = Project.objects.get(project_appli_student_id=student.id)
            project_name = srtp_project.project_name
            midterm = MidTerm.objects.get(project_belong_id = srtp_project.project_id)
            return render(request, 'stuSrtp/stuSrtpMidTermApply.html', context={'project_name': project_name,
                                                                                'midterm': midterm})

    def post(self, request):
        if session_judge(request):
            return HttpResponse('{"status": "fail", "msg": "/"}', content_type='application/json')
        else:
            student = Student.objects.get(student_id=request.session['user_id'])
            srtp_project = Project.objects.get(project_appli_student_id=student.id)
            midterm_file = request.FILES.get('file', '')
            file_detail = file_upload(midterm_file, 'SrtpMidTerm')
            midterm = MidTerm.objects.get(project_belong_id = srtp_project.project_id)
            midterm.midterm_file_name = file_detail[0]
            midterm.midterm_file_url = file_detail[1]
            midterm.midterm_check_status = '1'
            midterm.midterm_cehck_point = '1'
            midterm.save()
            return HttpResponse('{"status": "success", "msg": "添加成功"}', content_type='application/json')


class stuSrtpConcluApplyView(View):

    def get(self, request):
        if session_judge(request):
            return render(request, 'index.html')
        else:
            user_id = request.session['user_id']
            student = Student.objects.get(student_id=user_id)
            srtp_project = Project.objects.get(project_appli_student_id=student.id)
            project_name = srtp_project.project_name
            conclusion = Conclusion.objects.get(project_belong_id = srtp_project.project_id)
            return render(request, 'stuSrtp/stuSrtpConcluApply.html', context={'project_name': project_name,
                                                                               'conclusion': conclusion})

    def post(self, request):
        student = Student.objects.get(student_id=request.session['user_id'])
        srtp_project = Project.objects.get(project_appli_student_id=student.id)
        conclusion_file = request.FILES.get('file', '')
        file_detail = file_upload(conclusion_file, 'SrtpConclusion')
        conclusion = Conclusion.objects.get(project_belong_id=srtp_project.project_id)
        conclusion.conclusion_file_name = file_detail[0]
        conclusion.conclusion_file_url = file_detail[1]
        conclusion.conclusion_check_status = '1'
        conclusion.conclusion_check_point = '1'
        conclusion.save()
        return HttpResponse('{"status": "success", "msg": "添加成功"}', content_type='application/json')


class fileDownloadView(View):

    def get(self, request):
        if session_judge(request):
            return render(request, 'index.html')
        else:

            url = str(request.get_full_path())
            result = Result.objects.get(result_file_url = url)
            file_url = url.split('/')
            the_file_name = settings.MEDIA_ROOT + '/' + file_url[2] + '/' + file_url[3]
            response = StreamingHttpResponse(file_iterator(the_file_name))
            response['Content-Type'] = 'application/octet-stream'
            response['Content-Disposition'] = 'attachment; filename=%s' % str(result.result_file_name).encode('utf-8').decode('ISO-8859-1')
            return response


    def post(self, request):
        pass













