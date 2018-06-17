from course_arrangement.models import Selection
from django.db.models import Q

def course_capacity():

    room_list_1 = [1, 2, 3, 7]
    room_list_2 = [2, 4, 5]
    room_list_3 = [315, 415, 617, 619, 721, 724, 821, 824]

    # for room_1 in range(1, 8):
    #     for room_3 in room_list_1:
    #         room = room_1 * 100 + room_3
    #         if room == 103 or room == 203:
    #             continue
    #         selection_list = Selection.objects.filter(Q(course_building=1) & Q(course_classroom=room)).order_by('id')
    #         for selection in selection_list:
    #             selection.capacity = False
    #             print(selection.selection)
    #             selection.save()

    # for room_1 in range(1, 6):
    #     for room_3 in room_list_2:
    #         room = room_1 * 100 + room_3
    #         if room == 105 or room == 205 or room == 305:
    #             continue
    #         selection_list = Selection.objects.filter(Q(course_building=2) & Q(course_classroom=room)).order_by('id')
    #         for selection in selection_list:
    #             selection.capacity = False
    #             print(selection.selection)
    #             selection.save()
    #
    # for room in room_list_3:
    #     selection_list = Selection.objects.filter(Q(course_building=3) & Q(course_classroom=room)).order_by('id')
    #     for selection in selection_list:
    #         selection.capacity = False
    #         print(selection.selection)
    #         selection.save()


    # selection_list = Selection.objects.filter(Q(course_period=1) &
    #                                           Q(course_weekday=2) &
    #                                           Q(course_time=2) &
    #                                           Q(course_building=1) &
    #                                           Q(is_empty=False) &
    #                                           Q(capacity=True)).order_by('selection')
    # for selection in selection_list:
    #     selection.is_empty = True
    #     print(selection.selection)
    #     selection.save()

