from django.shortcuts import render
from django.views import View
from student.models import Student
from teacher.models import Teacher
from srtp_project.models import Project, Schedule, Fund, Result, AddFund, MidTerm, Conclusion
from main_platform.models import Notification, NotifiFile
from graduation_design.models import ModelFile, OpeningReport, MidtermReport, Dissertation
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
            return HttpResponse('{"status": "fail", "msg": "/"}', content_type='application/json')
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
            return HttpResponse('{"status": "fail", "msg": "/"}', content_type='application/json')
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
            return HttpResponse('{"status": "fail", "msg": "/"}', content_type='application/json')
        else:

            return render(request, 'teaSrtp/teaSrtpProManage.html')


class teaSrtpProListView(View):

    def get(self, request):
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
            return HttpResponse('{"status": "fail", "msg": "/"}', content_type='application/json')
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
