from django.shortcuts import render
from django.shortcuts import render
from django.views import View
from course_arrangement.models import Course, Selection
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q

# Create your views here.

class courseArrangementView(View):

    def get(self, request):
        course_list = Course.objects.all().order_by('-course_priority')
        for course in course_list:
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
        return HttpResponse('{"status": "sucess", "msg": "/"}', content_type='application/json')

    def post(self, request):
        pass