from django.shortcuts import render
from django.views import View
from student.models import Student
from teacher.models import Teacher
from srtp_project.models import Project, Schedule, Fund, Result, AddFund, MidTerm, Conclusion,Notification
from utils.session_judge import session_judge_teacher
from utils.file_utils import file_iterator, file_upload
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
import time, datetime, os
from django.db.models import Q
from pure_pagination import PageNotAnInteger, Paginator# Create your views here.


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

    def post(self, request):
        if session_judge_teacher(request):
            return HttpResponse('{"status": "fail", "msg": "/"}', content_type='application/json')
        else:
            return HttpResponse('{"status": "success", "msg": "success"}', content_type='application/json')


class teaSrtpProInfoView(View):

    def get(self, request, project_id):
        if session_judge_teacher(request):
            return HttpResponse('{"status": "fail", "msg": "/"}', content_type='application/json')
        else:
            srtp_project = Project.objects.get(project_id=project_id)
            teacher_uid = srtp_project.project_teacher_id
            teacher = Teacher.objects.get(id = teacher_uid)
            teacher_name = teacher.teacher_name
            return render(request, 'teaSrtp/teaSrtpProInfo.html', context={'srtp_project': srtp_project,
                                                                           'teacher_name': teacher_name})

    def post(self, request):
        pass


class teaSrtpScheduleManageView(View):

    def get(self, request):
        pass

    def post(self, request):
        pass


class teaSrtpFundManageView(View):

    def get(self, request):
        pass

    def post(self, request):
        pass


class teaSrtpResultManageView(View):

    def get(self, request):
        pass

    def post(self, request):
        pass


class teaSrtpAddtionFundsView(View):

    def get(self, request):
        pass

    def post(self, request):
        pass


class teaSrtpMidTermApplyView(View):

    def get(self, request):
        pass

    def post(self, request):
        pass


class teaSrtpConcluApplyView(View):

    def get(self, request):
        pass

    def post(self, request):
        pass


class teaSrtpProPublishView(View):

    def get(self, request):
        pass

    def post(self, request):
        pass


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
            return render(request, 'teaSrtp/teaSrtpNotification.html', context={'notification': notification,
                                                                                'project_view_list': project_view_list})


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
