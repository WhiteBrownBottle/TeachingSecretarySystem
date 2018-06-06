from django.shortcuts import render
from django.views import View
from student.models import Student
from teacher.models import Teacher
from srtp_project.models import Project, Schedule, Fund, Result, AddFund, MidTerm, Conclusion,Notification
from utils.session_judge import session_judge
from utils.file_utils import file_iterator, file_upload
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
import time, datetime, os
from django.db.models import Q
from pure_pagination import PageNotAnInteger, Paginator



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
            all_notification = Notification.objects.all().order_by("-notifi_date")
            # 分页：
            try:
                page = request.GET.get('page', '1')
            except PageNotAnInteger:
                page = 1
            p = Paginator(all_notification, 5, request=request)
            notification_list = p.page(page)
            return render(request, 'stuSrtp/stuSrtpHome.html', context={'notification_list': notification_list})

    def post(self, request):
        pass


class stuSrtpNotifiView(View):

    def get(self, request, notifi_id):
        if session_judge(request):
            return HttpResponse('{"status": "fail", "msg": "/"}', content_type='application/json')
        else:
            notification = Notification.objects.get(notifi_id = int(notifi_id))
            return render(request, 'stuSrtp/stuSrtpNotification.html', context={'notification': notification})





    def post(self, request, notifi_id):
        if session_judge(request):
            return HttpResponse('{"status": "fail", "msg": "/"}', content_type='application/json')
        else:
            notification = Notification.objects.get(notifi_id=int(notifi_id))
            return render(request, 'stuSrtp/stuSrtpNotification.html', context={'notification': notification})

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
            student = Student.objects.get(student_id = request.session['user_id'])
            member_num = int(request.POST.get('member_num', '0'))
            stuname_list = []
            stunumber_list = []
            member_list = ''
            if member_num != 0:
                for i in range(1, member_num+1):
                    if i > 1:
                        if i < member_num:
                            member_list = member_list + request.POST.get('stuname_%d' %(i), '') + '、'
                        else:
                            member_list += request.POST.get('stuname_%d' %(i), '')
                    stuname_list.append(request.POST.get('stuname_%d' %(i), ''))
                    stunumber_list.append(request.POST.get('number_%d' %(i), ''))
            applicant_phone = request.POST.get('phone', '')
            applicant_email = request.POST.get('email', '')
            if student.student_name != stuname_list[0] and student.student_id != int(stunumber_list[0]) and student.student_phone != applicant_phone and student.student_email != applicant_email:
                return HttpResponse('{"status": "fail", "msg": "申请人信息填写错误"}', content_type='application/json')
            else:
                srtp_project = Project()
                srtp_project.project_appli_student = student
                srtp_project.project_name = request.POST.get('proname', '')
                srtp_project.project_plan = request.POST.get('jihua', '')
                srtp_project.project_type = request.POST.get('cx', 'cx')
                srtp_project.project_rank = request.POST.get('rank', '1')
                srtp_project.project_depart = request.POST.get('depart', 'jt')
                srtp_project.project_fund_appli = int(request.POST.get('fund', '3000'))
                srtp_project.project_period = request.POST.get('zhouqi', '1年')
                srtp_project.project_form = request.POST.get('results', '实体')
                begin_date = request.POST.get('begin', datetime.datetime.now().strftime("%Y-%m-%d"))
                if begin_date != '':
                    begin_date = datetime.datetime.strptime(begin_date, "%Y-%m-%d").date()
                one_year = datetime.datetime.now() + datetime.timedelta(days=365)
                print(one_year)
                end_date = request.POST.get('end', one_year.strftime("%Y-%m-%d"))
                if end_date != '':
                    end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
                srtp_project.project_date_begin = begin_date
                srtp_project.project_date_end = end_date
                teacher_name = request.POST.get('teacher', '')
                teacher = Teacher.objects.get(teacher_name = teacher_name)
                srtp_project.project_teacher = teacher
                srtp_project.project_member = member_list
                appli_file = request.FILES.get('apply_file', '')
                file_detail = file_upload(appli_file, 'SrtpAppli')
                srtp_project.project_appli_name = file_detail[0]
                srtp_project.project_appli_url = file_detail[1]
                srtp_project.save()
                return HttpResponse('{"status": "success", "msg": "success"}', content_type='application/json')


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
            try:
                midterm = MidTerm.objects.get(project_belong_id = srtp_project.project_id)
            except MidTerm.DoesNotExist:
                midterm = None

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
            try:
                midterm = MidTerm.objects.get(project_belong_id = srtp_project.project_id)
            except MidTerm.DoesNotExist:
                midterm = MidTerm()
            midterm.midterm_file_name = file_detail[0]
            midterm.midterm_file_url = file_detail[1]
            midterm.midterm_check_status = '1'
            midterm.midterm_cehck_point = '1'
            midterm.project_belong = srtp_project
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
            try:
                conclusion = Conclusion.objects.get(project_belong_id = srtp_project.project_id)
            except Conclusion.DoesNotExist:
                conclusion = None
            return render(request, 'stuSrtp/stuSrtpConcluApply.html', context={'project_name': project_name,
                                                                               'conclusion': conclusion})

    def post(self, request):
        student = Student.objects.get(student_id=request.session['user_id'])
        srtp_project = Project.objects.get(project_appli_student_id=student.id)
        conclusion_file = request.FILES.get('file', '')
        file_detail = file_upload(conclusion_file, 'SrtpConclusion')
        try:
            conclusion = Conclusion.objects.get(project_belong_id=srtp_project.project_id)
        except Conclusion.DoesNotExist:
            conclusion = Conclusion()
        conclusion.conclusion_file_name = file_detail[0]
        conclusion.conclusion_file_url = file_detail[1]
        conclusion.conclusion_check_status = '1'
        conclusion.conclusion_check_point = '1'
        conclusion.project_belong = srtp_project
        conclusion.save()
        return HttpResponse('{"status": "success", "msg": "添加成功"}', content_type='application/json')

