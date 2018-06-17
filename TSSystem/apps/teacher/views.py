from django.shortcuts import render
from django.views import View
from student.models import Student
from teacher.models import Teacher
from srtp_project.models import Project, Schedule, Fund, Result, AddFund, MidTerm, Conclusion
from main_platform.models import Notification, NotifiFile
from graduation_design.models import ModelFile, OpeningReport, MidtermReport, Dissertation
from edu_reform.models import EduProject, EduMidTerm, EduConclusion, EduFund, EduResult
from course_arrangement.models import Selection, Course
from utils.session_judge import session_judge_teacher
from utils.file_utils import file_iterator, file_upload
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
import time, datetime, os
from django.db.models import Q
from pure_pagination import PageNotAnInteger, Paginator
# Create your views here.


class teaInfoView(View):

    def get(self, request):
        if session_judge_teacher(request):
            return HttpResponseRedirect('/')
        else:
            teacher = Teacher.objects.get(teacher_id=request.session['user_id'])
            return render(request, 'personInfo/teaInfo.html', context={'teacher': teacher})

    def post(self, request):
        if session_judge_teacher(request):
            return HttpResponse('{"status": "fail", "msg": "/"}', content_type='application/json')
        else:
            teacher = Teacher.objects.get(teacher_id=request.session['user_id'])
            return render(request, 'personInfo/teaInfo.html', context={'teacher': teacher})


class teaSrtpHomeView(View):

    def get(self, request):
        if session_judge_teacher(request):
            return HttpResponseRedirect('/')
        else:
            user_id = request.session['user_id']
            teacher = Teacher.objects.get(teacher_id=user_id)
            try:
                project_view_list = Project.objects.filter(Q(project_check_status=True) & Q(project_apply_status=False) & Q(
                    project_teacher_id=teacher.id)).order_by('project_id')
            except Project.DoesNotExist:
                project_view_list = None
            all_notification = Notification.objects.all().order_by("-notifi_date")
            # 分页：
            try:
                page = int(request.GET.get('page', '1'))
            except PageNotAnInteger:
                page = 1
            p = Paginator(all_notification, 5, request=request)
            notification_list = p.page(page)
            return render(request, 'teaSrtp/teaSrtpHome.html', context={'notification_list': notification_list,
                                                                        'project_view_list': project_view_list})

    def post(self, request):
        if session_judge_teacher(request):
            return HttpResponseRedirect('/')
        else:

            return render(request, 'teaSrtp/teaSrtpProManage.html')


class teaSrtpProListView(View):

    def get(self, request):
        if session_judge_teacher(request):
            return HttpResponseRedirect('/')
        else:
            user_id = request.session['user_id']
            teacher = Teacher.objects.get(teacher_id=user_id)
            try:
                project_view_list = Project.objects.filter(
                    Q(project_check_status=True) & Q(project_apply_status=False) & Q(
                        project_teacher_id=teacher.id)).order_by('project_id')
            except Project.DoesNotExist:
                project_view_list = None
            try:
                all_project = Project.objects.filter(Q(project_check_status=True) & Q(project_apply_status=False) & Q(project_teacher_id=teacher.id)).order_by('project_id')
            except Project.DoesNotExist:
                all_project = None
            try:
                page = int(request.GET.get('page', '1'))
            except PageNotAnInteger:
                page = 1
            p = Paginator(all_project, 5, request=request)
            project_list = p.page(page)
            return render(request, 'teaSrtp/teaSrtpProList.html', context={'project_list': project_list,
                                                                           'project_view_list': project_view_list})

    def post(self, request):
        if session_judge_teacher(request):
            return HttpResponse('{"status": "fail", "msg": "/"}', content_type='application/json')
        else:
            return render(request, 'teaSrtp/teaSrtpProManage.html')


class teaSrtpProManageView(View):

    def get(self, request, project_id):
        if session_judge_teacher(request):
            return HttpResponseRedirect('/')
        else:
            user_id = request.session['user_id']
            teacher = Teacher.objects.get(teacher_id=user_id)
            try:
                project_view_list = Project.objects.filter(
                    Q(project_check_status=True) & Q(project_apply_status=False) & Q(
                        project_teacher_id=teacher.id)).order_by('project_id')
            except Project.DoesNotExist:
                project_view_list = None
            srtp_project = Project.objects.get(project_id=project_id)
            addfund_checkok_list = AddFund.objects.filter(Q(project_belong_id=project_id)&Q(addfund_check_status = '1')&Q(addfund_add_status = '0'))
            if addfund_checkok_list != '':
                for addfund_checkok in addfund_checkok_list:
                    addfund_checkok_money = addfund_checkok.addfund_num
                    srtp_project.project_fund_approv += addfund_checkok_money
                    addfund_checkok.addfund_add_status = '1'
                    addfund_checkok.save()
            srtp_project.save()
            return render(request, 'teaSrtp/teaSrtpProManage.html', context={'srtp_project': srtp_project,
                                                                             'project_view_list': project_view_list})

    def post(self, request, project_id):
        if session_judge_teacher(request):
            return HttpResponse('{"status": "fail", "msg": "/"}', content_type='application/json')
        else:
            return HttpResponse('{"status": "success", "msg": "success"}', content_type='application/json')


class teaSrtpProInfoView(View):

    def get(self, request, project_id):
        if session_judge_teacher(request):
            return HttpResponse('{"status": "fail", "msg": "/"}', content_type='application/json')
        else:
            srtp_project = Project.objects.get(project_id = project_id)
            teacher_uid = srtp_project.project_teacher_id
            teacher = Teacher.objects.get(id = teacher_uid)
            teacher_name = teacher.teacher_name
            return render(request, 'teaSrtp/teaSrtpProInfo.html', context={'srtp_project': srtp_project,
                                                                           'teacher_name': teacher_name})

    def post(self, request):
        pass


class teaSrtpScheduleManageView(View):

    def get(self, request, project_id):
            if session_judge_teacher(request):
                return HttpResponse('{"status": "fail", "msg": "/"}', content_type='application/json')
            else:
                srtp_project = Project.objects.get(project_id = project_id)
                schedule_list = Schedule.objects.filter(project_belong_id=srtp_project.project_id).order_by(
                    'schedule_date')
                return render(request, 'teaSrtp/teaSrtpScheduleManage.html', context={'srtp_project': srtp_project,
                                                                                      'schedule_list': schedule_list})

    def post(self, request):
        pass


class teaSrtpFundManageView(View):

    def get(self, request, project_id):
        if session_judge_teacher(request):
            return HttpResponse('{"status": "fail", "msg": "/"}', content_type='application/json')
        else:
            srtp_project = Project.objects.get(project_id = project_id)
            fund_list = Fund.objects.filter(project_belong_id = srtp_project.project_id).order_by('fund_date')
            return render(request, 'teaSrtp/teaSrtpFundManage.html', context={'srtp_project': srtp_project,
                                                                              'fund_list': fund_list})

    def post(self, request):
        pass


class teaSrtpResultManageView(View):

    def get(self, request, project_id):
        if session_judge_teacher(request):
            return HttpResponse('{"status": "fail", "msg": "/"}', content_type='application/json')
        else:
            srtp_project = Project.objects.get(project_id=project_id)
            result_list = Result.objects.filter(project_belong_id=srtp_project.project_id).order_by('result_date')
            return render(request, 'teaSrtp/teaSrtpResultManage.html', context={'srtp_project': srtp_project,
                                                                                'result_list': result_list})

    def post(self, request):
        pass


class teaSrtpDeleteResultView(View):

    def get(self, request):
        if session_judge_teacher(request):
            return HttpResponseRedirect('/')
        else:
            pass

    def post(self, request):
        if session_judge_teacher(request):
            return HttpResponseRedirect('/')
        else:
            result_id = request.POST.get('result_id', '')
            Result.objects.get(id = result_id).delete()
            return HttpResponse('{"status": "success", "msg": "删除成功"}', content_type='application/json')


class teaSrtpAddtionFundsView(View):

    def get(self, request, project_id):
        if session_judge_teacher(request):
            return render(request, 'index.html')
        else:
            srtp_project = Project.objects.get(project_id=project_id)
            addfund_list = AddFund.objects.filter(project_belong_id = srtp_project.project_id).order_by('addfund_date')
            return render(request, 'teaSrtp/teaSrtpAddtionFunds.html', context={'srtp_project': srtp_project,
                                                                                'addfund_list': addfund_list})

    def post(self, request, project_id):
        if session_judge_teacher(request):
            return render(request, 'index.html')
        else:
            srtp_project = Project.objects.get(project_id=project_id)
            addfund_num = request.POST.get('fund', '0')
            addfund_reason = request.POST.get('addReason', '')
            addfund = AddFund()
            addfund.addfund_num = int(addfund_num)
            addfund.addfund_reason = addfund_reason
            addfund.project_belong = srtp_project
            addfund.save()
            return HttpResponse('{"status": "success", "msg": "添加成功"}', content_type='application/json')


class teaSrtpMidTermApplyView(View):

    def get(self, request, project_id):
        if session_judge_teacher(request):
            return render(request, 'index.html')
        else:
            srtp_project = Project.objects.get(project_id = project_id)
            project_name = srtp_project.project_name
            try:
                midterm = MidTerm.objects.get(project_belong_id = srtp_project.project_id)
            except MidTerm.DoesNotExist:
                midterm  = MidTerm()
                midterm.midterm_check_status = '0'
                midterm.midterm_cehck_point = '0'
                midterm.project_belong = srtp_project
                midterm.save()
            return render(request, 'teaSrtp/teaSrtpMidTermApply.html', context={'srtp_project': srtp_project,
                                                                                'midterm': midterm})

    def post(self, request, project_id):
        if session_judge_teacher(request):
            return HttpResponse('{"status": "fail", "msg": "/"}', content_type='application/json')
        else:
            srtp_project = Project.objects.get(project_id = project_id)
            midterm = MidTerm.objects.get(project_belong_id = project_id)
            midterm.midterm_check_point = '2'
            midterm.save()
            return HttpResponse('{"status": "success", "msg": "添加成功"}', content_type='application/json')


class teaSrtpConcluApplyView(View):

    def get(self, request, project_id):
        if session_judge_teacher(request):
            return render(request, 'index.html')
        else:
            srtp_project = Project.objects.get(project_id = project_id)
            project_name = srtp_project.project_name
            try:
                conclusion = Conclusion.objects.get(project_belong_id = srtp_project.project_id)
            except Conclusion.DoesNotExist:
                conclusion = Conclusion()
                conclusion.conclusion_check_status = '0'
                conclusion.conclusion_check_point = '0'
                conclusion.project_belong = srtp_project
                conclusion.save()
            return render(request, 'teaSrtp/teaSrtpConcluApply.html', context={'srtp_project': srtp_project,
                                                                               'conclusion': conclusion})

    def post(self, request, project_id):
        if session_judge_teacher(request):
            return HttpResponse('{"status": "fail", "msg": "/"}', content_type='application/json')
        else:
            srtp_project = Project.objects.get(project_id = project_id)
            conclusion = Conclusion.objects.get(project_belong_id = project_id)
            conclusion.conclusion_check_point = '2'
            conclusion.save()
            return HttpResponse('{"status": "success", "msg": "添加成功"}', content_type='application/json')


class teaSrtpProPublishView(View):

    def get(self, request):
        if session_judge_teacher(request):
            return render(request, 'index.html')
        else:
            return render(request, 'teaSrtp/teaSrtpProPublish.html')

    def post(self, request):
        if session_judge_teacher(request):
            return HttpResponse('{"status": "fail", "msg": "/"}', content_type='application/json')
        else:
            srtp_project = Project()
            srtp_project.project_name = request.POST.get('proname', '')
            srtp_project.project_plan = request.POST.get('jihua', '')
            srtp_project.project_subject = request.POST.get('xk', '')
            srtp_project.project_depart = request.POST.get('depart', 'jt')
            teacher_name = request.POST.get('teacher', '')
            teacher = Teacher.objects.get(teacher_name = teacher_name)
            teacher.teacher_phone = request.POST.get('phone', '')
            teacher.teacher_email = request.POST.get('email', '')
            srtp_project.project_teacher = teacher
            srtp_project.project_type = request.POST.get('type', 'cx')
            srtp_project.project_suggest_people_num = request.POST.get('suggest_people_num', '')
            srtp_project.project_intro = request.POST.get('intro', '')
            srtp_project.project_check_status = True
            teacher.save()
            srtp_project.save()
            return HttpResponse('{"status": "success", "msg": "success"}', content_type='application/json')


class teaSrtpNotifiView(View):

    def get(self, request, notifi_id):
        if session_judge_teacher(request):
            return HttpResponse('{"status": "fail", "msg": "/"}', content_type='application/json')
        else:
            user_id = request.session['user_id']
            teacher = Teacher.objects.get(teacher_id=user_id)
            try:
                project_view_list = Project.objects.filter(
                    Q(project_check_status=True) & Q(project_apply_status=False) & Q(
                        project_teacher_id=teacher.id)).order_by('project_id')
            except Project.DoesNotExist:
                project_view_list = None
            notification = Notification.objects.get(notifi_id = int(notifi_id))
            try:
                notifi_file_list = NotifiFile.objects.filter(notifi_belong = notification)
            except Notification.DoesNotExist:
                notifi_file_list = None
            return render(request, 'teaSrtp/teaSrtpNotification.html', context={'notification': notification,
                                                                                'project_view_list': project_view_list,
                                                                                'notifi_file_list': notifi_file_list})


    def post(self, request, notifi_id):
        if session_judge_teacher(request):
            return HttpResponse('{"status": "fail", "msg": "/"}', content_type='application/json')
        else:
            notification = Notification.objects.get(notifi_id=int(notifi_id))
            return render(request, 'teaSrtp/teaSrtpNotification.html', context={'notification': notification})
        pass


class teaSrtpSpecificInfoView(View):

    def get(self, request, project_id):
        if session_judge_teacher(request):
            return HttpResponseRedirect('/')
        else:
            project = Project.objects.get(project_id =int(project_id))
            return render(request, 'teaSrtp/teaSrtpSpecificInfo.html', context={'project': project})

    def post(self, request, project_id):
        if session_judge_teacher(request):
            return HttpResponse('{"status": "fail", "msg": "/"}', content_type='application/json')
        else:
            project = Project.objects.get(project_id =int(project_id))
            return render(request, 'teaSrtp/teaSrtpSpecificInfo.html', context={'project': project})


class teaGraHomeView(View):

    def get(self, request):
        if session_judge_teacher(request):
            return HttpResponseRedirect('/')
        else:
            all_notification = Notification.objects.all().order_by("-notifi_date")
            # 分页：
            try:
                page = int(request.GET.get('page', '1'))
            except PageNotAnInteger:
                page = 1
            p = Paginator(all_notification, 5, request=request)
            notification_list = p.page(page)
            return render(request, 'teaGra/teaGraHome.html', context={'notification_list': notification_list})

    def post(self, request):
        if session_judge_teacher(request):
            return HttpResponseRedirect('/')
        else:
            self.get(request)


class teaGraNotifiView(View):

    def get(self, request, notifi_id):
        if session_judge_teacher(request):
            return HttpResponseRedirect('/')
        else:

            notification = Notification.objects.get(notifi_id = int(notifi_id))
            try:
                notifi_file_list = NotifiFile.objects.filter(notifi_belong = notification)
            except Notification.DoesNotExist:
                notifi_file_list = None
            return render(request, 'teaGra/teaGraNotification.html', context={'notification': notification,
                                                                                'notifi_file_list': notifi_file_list})


    def post(self, request, notifi_id):
        if session_judge_teacher(request):
            return HttpResponseRedirect('/')
        else:
            notification = Notification.objects.get(notifi_id=int(notifi_id))
            return render(request, 'teaGra/teaGraNotification.html', context={'notification': notification})


class teaGraModelfileView(View):

    def get(self, request):
        if session_judge_teacher(request):
            return HttpResponseRedirect('/')

        else:
            modelfile_list = ModelFile.objects.all().order_by('id')
            return render(request, 'teaGra/teaGraModelfiledownload.html', context={'modelfile_list': modelfile_list})

    def post(self, request):
        if session_judge_teacher(request):
            return HttpResponseRedirect('/')

        else:
            modelfile_list = ModelFile.objects.all().order_by('id')
            return render(request, 'teaGra/teaGraModelfiledownload.html', context={'modelfile_list': modelfile_list})


class teaGraProposalView(View):

    def get(self, request):
        if session_judge_teacher(request):
            return HttpResponseRedirect('/')
        else:
            user_id = request.session['user_id']
            teacher = Teacher.objects.get(teacher_id = user_id)
            openingreport_list = OpeningReport.objects.filter(teacher_to_id = teacher.id).order_by('file_date')
            return render(request, 'teaGra/teaGraProposal.html', context={'openingreport_list':openingreport_list })

    def post(self, request):
        if session_judge_teacher(request):
            return HttpResponseRedirect('/')
        else:
            user_id = request.session['user_id']
            teacher = Teacher.objects.get(teacher_id=user_id)
            openingreport = OpeningReport()
            proposal_file = request.FILES.get('kaiti_file', '')
            file_detail = file_upload(proposal_file, 'GradOpeningCollection')
            openingreport.file_name = file_detail[0]
            openingreport.file_url = file_detail[1]
            openingreport.teacher_to = teacher
            openingreport.save()
            return HttpResponse('{"status": "success", "msg": "添加成功"}', content_type='application/json')


class teaGraMidtermView(View):

    def get(self, request):
        if session_judge_teacher(request):
            return HttpResponseRedirect('/')
        else:
            user_id = request.session['user_id']
            teacher = Teacher.objects.get(teacher_id=user_id)
            midtermreport_list = MidtermReport.objects.filter(teacher_to_id = teacher.id).order_by('file_date')
            return render(request, 'teaGra/teaGraMidterm.html', context={'midtermreport_list': midtermreport_list})

    def post(self, request):
        if session_judge_teacher(request):
            return HttpResponseRedirect('/')
        else:
            user_id = request.session['user_id']
            teacher = Teacher.objects.get(teacher_id=user_id)
            midtermreport = MidtermReport()
            midterm_file = request.FILES.get('mid_file', '')
            file_detail = file_upload(midterm_file, 'GradMidtermCollection')
            midtermreport.file_name = file_detail[0]
            midtermreport.file_url = file_detail[1]
            midtermreport.teacher_to = teacher
            midtermreport.save()
            return HttpResponse('{"status": "success", "msg": "添加成功"}', content_type='application/json')


class teaGraPaperView(View):

    def get(self, request):
        if session_judge_teacher(request):
            return HttpResponseRedirect('/')
        else:
            user_id = request.session['user_id']
            teacher = Teacher.objects.get(teacher_id=user_id)
            dissertation_list = Dissertation.objects.filter(teacher_to_id = teacher.id).order_by('file_date')
            return render(request, 'teaGra/teaGraPaper.html', context={'dissertation_list': dissertation_list})

    def post(self, request):
        if session_judge_teacher(request):
            return HttpResponseRedirect('/')
        else:
            user_id = request.session['user_id']
            teacher = Teacher.objects.get(teacher_id=user_id)
            dissertation_list = Dissertation.objects.filter(teacher_to_id = teacher.id).order_by('file_date')
            return render(request, 'teaGra/teaGraPaper.html', context={'dissertation_list': dissertation_list})


class eduReformApplyView(View):

    def get(self, request):
        if session_judge_teacher(request):
            return render(request, 'index.html')
        else:
            return render(request, 'eduReform/eduReformApply.html')

    def post(self, request):
        if session_judge_teacher(request):
            return HttpResponse('{"status": "fail", "msg": "/"}', content_type='application/json')
        else:
            member_num = int(request.POST.get('member_num', '0'))
            peopleName_list = []
            peopleDuty_list = []
            member_list = ''
            if member_num != 0:
                for i in range(1, member_num+1):
                    if i > 1:
                        if i < member_num:
                            member_list = member_list + request.POST.get('peopleName_%d' %(i), '') + '、'
                        else:
                            member_list += request.POST.get('peopleName_%d' %(i), '')
                    peopleName_list.append(request.POST.get('peopleName_%d' %(i), ''))
                    peopleDuty_list.append(request.POST.get('peopleDuty_%d' %(i), ''))
            edu_project = EduProject()
            edu_project.eduproject_name = request.POST.get('pro_name', '')
            edu_project.eduproject_belong_unit = request.POST.get('work_unit', '')
            edu_project.eduproject_fund_appli = request.POST.get('fund', '')
            edu_project.eduproject_type = request.POST.get('type', 'zd')
            edu_project.eduproject_date_begin = request.POST.get('begin_date', '')
            edu_project.eduproject_date_end = request.POST.get('end_date', '')
            person_in_charge_name = request.POST.get('peopleName_1', '')
            teacher = Teacher.objects.get(teacher_name = person_in_charge_name)
            edu_project.eduproject_person_in_charge = teacher
            teacher.teacher_gender = request.POST.get('gender', '')
            teacher.teacher_birth_date = request.POST.get('birth_date', '')
            teacher.teacher_major = request.POST.get('major', '')
            teacher.teacher_title = request.POST.get('title', '')
            teacher.teacher_duty = request.POST.get('peopleDuty_1', '')
            teacher.teacher_phone = request.POST.get('phone', '')
            teacher.teacher_email = request.POST.get('email', '')
            appli_file = request.FILES.get('apply_file', '')
            file_detail = file_upload(appli_file, 'EduReformApply')
            edu_project.eduproject_appli_name= file_detail[0]
            edu_project.eduproject_appli_url = file_detail[1]
            edu_project.eduproject_member = member_list
            teacher.save()
            edu_project.save()
            return HttpResponse('{"status": "success", "msg": "success"}', content_type='application/json')


class eduReformConcluApplyView(View):

    def get(self, request, eduproject_id):
        if session_judge_teacher(request):
            return render(request, 'index.html')
        else:
            edu_project = EduProject.objects.get(eduproject_id = eduproject_id)
            eduproject_name = edu_project.eduproject_name
            try:
                educonclusion = EduConclusion.objects.get(eduproject_belong_id = edu_project.eduproject_id)
            except EduConclusion.DoesNotExist:
                educonclusion  = EduConclusion()
                educonclusion.educonclusion_check_status = '0'
                educonclusion.eduproject_belong = edu_project
                educonclusion.save()
            return render(request, 'eduReform/eduReformConcluApply.html', context={'edu_project': edu_project,
                                                                                   'educonclusion': educonclusion})

    def post(self, request, eduproject_id):
        if session_judge_teacher(request):
            return HttpResponse('{"status": "fail", "msg": "/"}', content_type='application/json')
        else:
            edu_project = EduProject.objects.get(eduproject_id = eduproject_id)
            educonclusion_file = request.FILES.get('file', '')
            file_detail = file_upload(educonclusion_file, 'EduConclusion')
            educonclusion = EduConclusion.objects.get(eduproject_belong_id = eduproject_id)
            educonclusion.educonclusion_file_name = file_detail[0]
            educonclusion.educonclusion_file_url = file_detail[1]
            educonclusion.educonclusion_check_status = '1'
            educonclusion.eduproject_belong = edu_project
            educonclusion.save()
            return HttpResponse('{"status": "success", "msg": "添加成功"}', content_type='application/json')


class eduReformHomeView(View):

    def get(self, request):
        if session_judge_teacher(request):
            return HttpResponseRedirect('/')
        else:
            user_id = request.session['user_id']
            teacher = Teacher.objects.get(teacher_id = user_id)
            try:
                eduproject_view_list = EduProject.objects.filter(Q(eduproject_person_in_charge_id = teacher.id)).order_by('eduproject_id')
            except EduProject.DoesNotExist:
                eduproject_view_list = None
            all_notification = Notification.objects.all().order_by("-notifi_date")
            # 分页：
            try:
                page = int(request.GET.get('page', '1'))
            except PageNotAnInteger:
                page = 1
            p = Paginator(all_notification, 5, request=request)
            notification_list = p.page(page)
            return render(request, 'eduReform/eduReformHome.html', context={'notification_list': notification_list,
                                                                        'eduproject_view_list': eduproject_view_list})

    def post(self, request):
        if session_judge_teacher(request):
            return HttpResponse('{"status": "fail", "msg": "/"}', content_type='application/json')
        else:

            return render(request, 'eduReform/eduReformHome.html')


class eduReformInfoView(View):

    def get(self, request, eduproject_id):
        if session_judge_teacher(request):
            return HttpResponse('{"status": "fail", "msg": "/"}', content_type='application/json')
        else:
            edu_project = EduProject.objects.get(eduproject_id = eduproject_id)
            teacher_uid = edu_project.eduproject_person_in_charge_id
            teacher = Teacher.objects.get(id = teacher_uid)
            return render(request, 'eduReform/eduReformInfo.html', context={'edu_project': edu_project,
                                                                            'teacher': teacher})

    def post(self, request):
        pass


class eduReformManageView(View):

    def get(self, request, eduproject_id):
        if session_judge_teacher(request):
            return HttpResponseRedirect('/')
        else:
            user_id = request.session['user_id']
            teacher = Teacher.objects.get(teacher_id = user_id)
            try:
                eduproject_view_list = EduProject.objects.filter(Q(eduproject_person_in_charge_id = teacher.id)).order_by('eduproject_id')
            except EduProject.DoesNotExist:
                eduproject_view_list = None
            edu_project = EduProject.objects.get(eduproject_id = eduproject_id)
            return render(request, 'eduReform/eduReformManage.html', context={'edu_project': edu_project,
                                                                        'eduproject_view_list': eduproject_view_list})


class eduReformMidTermApplyView(View):

    def get(self, request, eduproject_id):
        if session_judge_teacher(request):
            return render(request, 'index.html')
        else:
            edu_project = EduProject.objects.get(eduproject_id = eduproject_id)
            eduproject_name = edu_project.eduproject_name
            try:
                edumidterm = EduMidTerm.objects.get(eduproject_belong_id = edu_project.eduproject_id)
            except EduMidTerm.DoesNotExist:
                edumidterm  = EduMidTerm()
                edumidterm.edumidterm_check_status = '0'
                edumidterm.eduproject_belong = edu_project
                edumidterm.save()
            return render(request, 'eduReform/eduReformMidTermApply.html', context={'edu_project': edu_project,
                                                                                    'edumidterm': edumidterm})

    def post(self, request, eduproject_id):
        if session_judge_teacher(request):
            return HttpResponseRedirect('/')
        else:
            edu_project = EduProject.objects.get(eduproject_id = eduproject_id)
            edumidterm_file = request.FILES.get('file', '')
            file_detail = file_upload(edumidterm_file, 'EduMidTerm')
            edumidterm = EduMidTerm.objects.get(eduproject_belong_id = eduproject_id)
            edumidterm.edumidterm_file_name = file_detail[0]
            edumidterm.edumidterm_file_url = file_detail[1]
            edumidterm.edumidterm_check_status = '1'
            edumidterm.eduproject_belong = edu_project
            edumidterm.save()
            return HttpResponse('{"status": "success", "msg": "添加成功"}', content_type='application/json')


class eduReformFundManageView(View):

    def get(self, request, eduproject_id):
        if session_judge_teacher(request):
            return HttpResponseRedirect('/')
        else:
            edu_project = EduProject.objects.get(eduproject_id = eduproject_id)
            edufund_list = EduFund.objects.filter(eduproject_belong_id = edu_project.eduproject_id).order_by('edufund_date')
            return render(request, 'eduReform/eduReformFundManage.html', context={'edu_project': edu_project,
                                                                                  'edufund_list': edufund_list})

    def post(self, request, eduproject_id):
        if session_judge_teacher(request):
            return HttpResponseRedirect('/')
        else:
            edufund_time = request.POST.get('riqi', datetime.datetime.now().strftime("%Y-%m-%d"))
            if edufund_time != '':
                edufund_date = datetime.datetime.strptime(edufund_time, "%Y-%m-%d").date()
            edufund_name = request.POST.get('jutizhichu', '')
            edufund_type = request.POST.get('leibie', '12')
            edufund_num = int(request.POST.get('jine', ''))
            teacher = Teacher.objects.get(teacher_id=request.session['user_id'])
            edu_project = EduProject.objects.get(eduproject_person_in_charge_id=teacher.id)
            edufund = EduFund()
            edufund.edufund_name = edufund_name
            edufund.edufund_type = edufund_type
            edufund.edufund_num = edufund_num
            edufund.edufund_date = edufund_date
            edufund.eduproject_belong = edu_project
            edufund.save()
            return HttpResponse('{"status": "success", "msg": "添加成功"}', content_type='application/json')


class eduReformResultManageView(View):

    def get(self, request, eduproject_id):
        if session_judge_teacher(request):
            return HttpResponseRedirect('/')
        else:
            edu_project = EduProject.objects.get(eduproject_id = eduproject_id)
            eduresult_list = EduResult.objects.filter(eduproject_belong_id = edu_project.eduproject_id).order_by('eduresult_date')
            return render(request, 'eduReform/eduReformFundManage.html', context={'edu_project': edu_project,
                                                                                  'eduresult_list': eduresult_list})


    def post(self, request, eduproject_id):
        if session_judge_teacher(request):
            return HttpResponseRedirect('/')
        else:
            eduresult_name = request.POST.get('mingcheng' '')
            eduresult_type = request.POST.get('leixing', '7')
            eduresult_date = request.POST.get('riqi', datetime.datetime.now().strftime("%Y-%m-%d"))
            if eduresult_date != '':
                eduresult_date = datetime.datetime.strptime(eduresult_date, '%Y-%m-%d').date()
            eduresult_master = request.POST.get('suoyouren', '')
            eduresult_file = request.FILES.get('file')
            edufile_detail = file_upload(eduresult_file, 'EduResult')
            teacher = Teacher.objects.get(teacher_id=request.session['user_id'])
            edu_project = EduProject.objects.get(eduproject_person_in_charge_id=teacher.id)
            eduresult = EduResult()
            eduresult.eduresult_name = eduresult_name
            eduresult.eduresult_type = eduresult_type
            eduresult.eduresult_date = eduresult_date
            eduresult.eduresult_master = eduresult_master
            eduresult.eduresult_file_name = edufile_detail[0]
            eduresult.eduresult_file_url = edufile_detail[1]
            eduresult.eduproject_belong = edu_project
            eduresult.save()
            return HttpResponse('{"status": "success", "msg": "添加成功"}', content_type='application/json')


class eduReformDeleteResultView(View):

    def get(self, request):
        if session_judge_teacher(request):
            return HttpResponseRedirect('/')
        else:
            pass

    def post(self, request):
        result_id = request.POST.get('result_id', '')
        EduResult.objects.get(id = result_id).delete()
        return HttpResponse('{"status": "success", "msg": "删除成功"}', content_type='application/json')


class courseArrangementHome(View):

    def get(self, request, course_id):
        if session_judge_teacher(request):
            return HttpResponseRedirect('/')
        else:
            user_id = request.session['user_id']
            teacher = Teacher.objects.get(teacher_id = user_id)
            try:
                # course = Course.objects.filter(Q(course_teacher_id = teacher.id)).first()
                course_list = Course.objects.filter(Q(course_teacher_id = teacher.id)).order_by('course_id')
            except Course.DoesNotExist:
                # course = None
                course_list = None
            return render(request, 'courseArrangement/courseArrangementHome.html', context={'course_list': course_list,
                                                                                            'course_id': course_id})

    def post(self, request, course_id):
        if session_judge_teacher(request):
            return HttpResponse('{"status": "fail", "msg": "/"}', content_type='application/json')
        else:
            course_id = request.POST.get('course_id', '')
            course = Course.objects.get(course_id = course_id)
            if course.course_selection_1 != None:
                return HttpResponse('{"status": "fail", "msg": "您已经提交课程安排期望"}', content_type='application/json')
            course_point = course.course_point
            period_1 = int(request.POST.get('period_1', '1'))
            weekday_1 = int(request.POST.get('weekday_1', '1'))
            time_1 = int(request.POST.get('time_1', '1'))
            building_1 = int(request.POST.get('building_1', '1'))
            period_2 = int(request.POST.get('period_2', '0'))
            weekday_2 = int(request.POST.get('weekday_2', '0'))
            time_2 = int(request.POST.get('time_2', '0'))
            building_2 = int(request.POST.get('building_2', '0'))
            point_temp = 0
            if period_1 == 1 or period_1 == 2:
                point_temp += 16
            else:
                point_temp += 32
            if period_2 == 0:
                point_temp += 0
            elif period_2 == 1 or period_2 == 2:
                point_temp += 16
            else:
                point_temp += 32
            if point_temp != course_point:
                return HttpResponse('{"status": "fail", "msg": "提交错误，学时不匹配"}', content_type='application/json')
            period_list = [10, 20, 30, 11, 22, 33]
            if (period_1 * 10 + period_2) not in period_list:
                return HttpResponse('{"status": "fail", "msg": "请安排在相同周数"}', content_type='application/json')
            if period_1 == 1 or period_1 == 2:
                if building_1 == 1:
                    course_classroom = 805
                elif building_1 == 2:
                    course_classroom = 505
                elif building_1 == 3:
                    course_classroom = 824
                selection = Selection.objects.get(Q(course_period=period_1) & Q(course_weekday=weekday_1) & Q(course_time=time_1) & Q(course_building=building_1) & Q(course_classroom=course_classroom))
                course.course_selection_1 = selection
            if period_1 == 3:
                if building_1 == 1:
                    course_classroom = 805
                elif building_1 == 2:
                    course_classroom = 505
                elif building_1 == 3:
                    course_classroom = 824
                selection_list = Selection.objects.filter(Q(course_weekday=weekday_1) & Q(course_time=time_1) & Q(course_building=building_1) & Q(course_classroom=course_classroom))
                course.course_selection_1 = selection_list[0]
                course.course_selection_2 = selection_list[1]
            if period_2 == 1 or period_2 == 2:
                if building_2 == 1:
                    course_classroom = 805
                elif building_2 == 2:
                    course_classroom = 505
                elif building_2 == 3:
                    course_classroom = 824
                selection = Selection.objects.get(Q(course_period=period_2) & Q(course_weekday=weekday_2) & Q(course_time=time_2) & Q(course_building=building_2) & Q(course_classroom=course_classroom))
                course.course_selection_2 = selection
            if period_2 == 3:
                if building_2 == 1:
                    course_classroom = 805
                elif building_2 == 2:
                    course_classroom = 505
                elif building_2 == 3:
                    course_classroom = 824
                selection_list_2 = Selection.objects.filter(Q(course_weekday=weekday_2) & Q(course_time=time_2) & Q(course_building=building_2) & Q(course_classroom=course_classroom))
                course.course_selection_3 = selection_list_2[0]
                course.course_selection_4 = selection_list_2[1]
            course.save()
            return HttpResponse('{"status": "success", "msg": "success"}', content_type='application/json')


class courseArrangementInfo(View):

    def get(self, request, course_id):
        if session_judge_teacher(request):
            return HttpResponseRedirect('/')
        else:
            course = Course.objects.get(course_id = course_id)
            return render(request, 'courseArrangement/courseArrangementInfo.html', context={'course': course})

    def post(self, request):
        pass


class courseTable(View):

    def get(self, request):
        if session_judge_teacher(request):
            return HttpResponseRedirect('/')
        else:
            user_id = request.session['user_id']
            teacher = Teacher.objects.get(teacher_id = user_id)
            try:
                course_list = Course.objects.filter(Q(course_teacher_id = teacher.id)).order_by('course_id')
            except Course.DoesNotExist:
                course_list = None
            return render(request, 'courseArrangement/courseTable.html', context={'course_list': course_list,
                                                                                  'teacher': teacher})

    def post(self, request):
        pass