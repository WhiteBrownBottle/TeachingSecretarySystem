from django.shortcuts import render
from django.shortcuts import render
from django.views import View
from course_arrangement.models import Course, Selection, GetTeacherCourse
from teacher.models import Teacher
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q


# Create your views here.

class courseArrangementAdminView(View):

    def get(self, request):
        teacher_list = Teacher.objects.all().order_by('teacher_id')
        course_list = Course.objects.all().order_by('-course_priority')
        is_arranged = 1
        all_teacher_is_submit = 1
        for course in course_list:
            if course.course_selection_1 == None:
                all_teacher_is_submit = 0
                break
        for course in course_list:
            if course.is_arranged == False:
                is_arranged = 0
                break
        get_teacher_course = GetTeacherCourse.objects.get(id = 1)
        teacher_id = get_teacher_course.teacher_id
        try:
            teacher = Teacher.objects.get(teacher_id=teacher_id)
        except Teacher.DoesNotExist:
            teacher = None
        try:
            course_list = Course.objects.filter(Q(course_teacher_id=teacher.id)).order_by('course_id')
        except Course.DoesNotExist:
            course_list = None
        return render(request, 'courseArrangement/courseArrangementAdmin.html', context={'teacher_list': teacher_list,
                                                                                         'is_arranged': is_arranged,
                                                                                         'all_teacher_is_submit': all_teacher_is_submit,
                                                                                         'course_list': course_list,
                                                                                         'teacher': teacher})

    def post(self, request):
        teacher_id = request.POST.get('teacher_id', '')
        get_teacher_course = GetTeacherCourse.objects.get(id = 1)
        get_teacher_course.teacher_id = teacher_id
        get_teacher_course.save()
        return HttpResponse('{"status": "success", "msg": "/"}', content_type='application/json')


class courseArrangementView(View):

    def get(self, request):
        pass

    def post(self, request):
        flag = 0
        course_list = Course.objects.all().order_by('-course_priority')
        for course in course_list:
            if course.is_arranged == True:
                flag = 1
                continue
            course_selection = [course.course_selection_1, course.course_selection_2, course.course_selection_3, course.course_selection_4]
            for i in range(0, 4):
                if course_selection[i] == None:
                    continue
                empty_selection = Selection.objects.filter(Q(course_period=course_selection[i].course_period) &
                                                      Q(course_weekday=course_selection[i].course_weekday) &
                                                      Q(course_time=course_selection[i].course_time) &
                                                      Q(course_building=course_selection[i].course_building) &
                                                      Q(is_empty=True) &
                                                      Q(capacity=course.course_capacity > 50)).order_by('selection').first()
                if empty_selection == None:
                    empty_selection = Selection.objects.filter(Q(course_period=course_selection[i].course_period) &
                                                               Q(course_weekday=course_selection[i].course_weekday) &
                                                               Q(course_time=course_selection[i].course_time) &
                                                               ~Q(course_building=course_selection[i].course_building) &
                                                               Q(is_empty=True) &
                                                               Q(capacity=course.course_capacity > 50)).order_by('selection').first()
                if empty_selection == None:
                    empty_selection = Selection.objects.filter(Q(course_period=course_selection[i].course_period) &
                                                               Q(course_weekday=course_selection[i].course_weekday) &
                                                               ~Q(course_time=course_selection[i].course_time) &
                                                               Q(course_building=course_selection[i].course_building) &
                                                               Q(is_empty=True) &
                                                               Q(capacity=course.course_capacity > 50)).order_by('selection').first()
                    if empty_selection == None:
                        empty_selection = Selection.objects.filter(Q(course_period=course_selection[i].course_period) &
                                                                   Q(course_weekday=course_selection[i].course_weekday) &
                                                                   ~Q(course_time=course_selection[i].course_time) &
                                                                   ~Q(course_building=course_selection[i].course_building) &
                                                                   Q(is_empty=True) &
                                                                   Q(capacity=course.course_capacity > 50)).order_by('selection').first()
                if empty_selection == None:
                    empty_selection = Selection.objects.filter(Q(course_period=course_selection[i].course_period) &
                                                               ~Q(course_weekday=course_selection[i].course_weekday) &
                                                               Q(course_time=course_selection[i].course_time) &
                                                               Q(course_building=course_selection[i].course_building) &
                                                               Q(is_empty=True) &
                                                               Q(capacity=course.course_capacity > 50)).order_by('selection').first()
                    if empty_selection == None:
                        empty_selection = Selection.objects.filter(Q(course_period=course_selection[i].course_period) &
                                                                   ~Q(course_weekday=course_selection[i].course_weekday) &
                                                                   Q(course_time=course_selection[i].course_time) &
                                                                   ~Q(course_building=course_selection[i].course_building) &
                                                                   Q(is_empty=True) &
                                                                   Q(capacity=course.course_capacity > 50)).order_by('selection').first()
                    if empty_selection == None:
                        empty_selection = Selection.objects.filter(Q(course_period=course_selection[i].course_period) &
                                                                   ~Q(course_weekday=course_selection[i].course_weekday) &
                                                                   ~Q(course_time=course_selection[i].course_time) &
                                                                   Q(course_building=course_selection[i].course_building) &
                                                                   Q(is_empty=True) &
                                                                   Q(capacity=course.course_capacity > 50)).order_by('selection').first()
                    if empty_selection == None:
                        empty_selection = Selection.objects.filter(Q(course_period=course_selection[i].course_period) &
                                                                   ~Q(course_weekday=course_selection[i].course_weekday) &
                                                                   ~Q(course_time=course_selection[i].course_time) &
                                                                   ~Q(course_building=course_selection[i].course_building) &
                                                                   Q(is_empty=True) &
                                                                   Q(capacity=course.course_capacity > 50)).order_by('selection').first()
                if empty_selection == None:
                    empty_selection = Selection.objects.filter(~Q(course_period=course_selection[i].course_period) &
                                                               Q(course_weekday=course_selection[i].course_weekday) &
                                                               Q(course_time=course_selection[i].course_time) &
                                                               Q(course_building=course_selection[i].course_building) &
                                                               Q(is_empty=True) &
                                                               Q(capacity=course.course_capacity > 50)).order_by('selection').first()
                    if empty_selection == None:
                        empty_selection = Selection.objects.filter(~Q(course_period=course_selection[i].course_period) &
                                                                   Q(course_weekday=course_selection[i].course_weekday) &
                                                                   Q(course_time=course_selection[i].course_time) &
                                                                   ~Q(course_building=course_selection[i].course_building) &
                                                                   Q(is_empty=True) &
                                                                   Q(capacity=course.course_capacity > 50)).order_by('selection').first()
                    if empty_selection == None:
                        empty_selection = Selection.objects.filter(~Q(course_period=course_selection[i].course_period) &
                                                                   Q(course_weekday=course_selection[i].course_weekday) &
                                                                   ~Q(course_time=course_selection[i].course_time) &
                                                                   Q(course_building=course_selection[i].course_building) &
                                                                   Q(is_empty=True) &
                                                                   Q(capacity=course.course_capacity > 50)).order_by('selection').first()
                    if empty_selection == None:
                        empty_selection = Selection.objects.filter(~Q(course_period=course_selection[i].course_period) &
                                                                   Q(course_weekday=course_selection[i].course_weekday) &
                                                                   ~Q(course_time=course_selection[i].course_time) &
                                                                   ~Q(course_building=course_selection[i].course_building) &
                                                                   Q(is_empty=True) &
                                                                   Q(capacity=course.course_capacity > 50)).order_by('selection').first()
                    if empty_selection == None:
                        empty_selection = Selection.objects.filter(~Q(course_period=course_selection[i].course_period) &
                                                                   ~Q(course_weekday=course_selection[i].course_weekday) &
                                                                   Q(course_time=course_selection[i].course_time) &
                                                                   Q(course_building=course_selection[i].course_building) &
                                                                   Q(is_empty=True) &
                                                                   Q(capacity=course.course_capacity > 50)).order_by('selection').first()
                    if empty_selection == None:
                        empty_selection = Selection.objects.filter(~Q(course_period=course_selection[i].course_period) &
                                                                   ~Q(course_weekday=course_selection[i].course_weekday) &
                                                                   Q(course_time=course_selection[i].course_time) &
                                                                   ~Q(course_building=course_selection[i].course_building) &
                                                                   Q(is_empty=True) &
                                                                   Q(capacity=course.course_capacity > 50)).order_by('selection').first()
                    if empty_selection == None:
                        empty_selection = Selection.objects.filter(~Q(course_period=course_selection[i].course_period) &
                                                                   ~Q(course_weekday=course_selection[i].course_weekday) &
                                                                   ~Q(course_time=course_selection[i].course_time) &
                                                                   Q(course_building=course_selection[i].course_building) &
                                                                   Q(is_empty=True) &
                                                                   Q(capacity=course.course_capacity > 50)).order_by('selection').first()
                    if empty_selection == None:
                        empty_selection = Selection.objects.filter(~Q(course_period=course_selection[i].course_period) &
                                                                   ~Q(course_weekday=course_selection[i].course_weekday) &
                                                                   ~Q(course_time=course_selection[i].course_time) &
                                                                   ~Q(course_building=course_selection[i].course_building) &
                                                                   Q(is_empty=True) &
                                                                   Q(capacity=course.course_capacity > 50)).order_by('selection').first()
                course_selection[i] = empty_selection
                empty_selection.is_empty = False
                empty_selection.save()
            course.course_selection_1 = course_selection[0]
            course.course_selection_2 = course_selection[1]
            course.course_selection_3 = course_selection[2]
            course.course_selection_4 = course_selection[3]
            course.is_arranged = True
            course.save()
            print('"' + course.course_name + '"' + "已完成排课")
        if flag == 1:
            return HttpResponse('{"status": "success", "msg": "自动排课已完成"}', content_type='application/json')
        return HttpResponse('{"status": "success", "msg": "自动排课已完成"}', content_type='application/json')