from course_arrangement.models import Selection

def creat_course_selection():

    # room_list = [203, 314, 315, 414, 415, 616, 617, 619, 720, 721, 724, 820, 821, 824]

    for i in range(1, 3):
        for j in range(1, 6):
            for z in range(1, 7):
                # for x in room_list:
                # ------
                # for room_1 in range(1,6):
                #     for room_3 in range(1,6):
                #         room = room_1 * 100 + room_3
                #         if room == 105 or room == 205 or room == 305:
                #             continue
                # ------
                selection = Selection()
                selection.course_period = i
                selection.course_weekday = j
                selection.course_time = z
                selection.course_building = 3
                selection.course_classroom = x
                selection.is_empty = True
                print(1)
                selection.save()

