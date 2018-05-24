from django.db import models

# Create your models here.


class CourseTime(models.Model):

    COURSE_WEEKDAY_CHOICE = (
        ('1', '星期一'),
        ('2', '星期二'),
        ('3', '星期三'),
        ('4', '星期四'),
        ('5', '星期五'),
    )

    COURSETIME_CHOICE = (
        ('1', '第一节'),
        ('2', '第二节'),
        ('3', '第三节'),
        ('4', '第四节'),
        ('5', '第五节'),
        ('6', '第六节')
    )
    course_weekday = models.CharField(null=False, blank=False, choices=COURSE_WEEKDAY_CHOICE, max_length=1, default='1', verbose_name=u'上课时间(星期几)')
    course_time = models.CharField(null=False, blank=False, choices=COURSETIME_CHOICE, max_length=1, default='1', verbose_name=u'上课时间(第几节）')

    class Meta:
        verbose_name = u'上课时间'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '[%s: %s]' % (self.get_course_weekday_display(), self.get_course_time_display())


class Course(models.Model):

    WEEK_CHOICE = (
        ('week1', '第一周'),
        ('week2', '第二周'),
        ('week3', '第三周'),
        ('week4', '第四周'),
        ('week5', '第五周'),
        ('week6', '第六周'),
        ('week7', '第七周'),
        ('week8', '第八周'),
        ('week9', '第九周'),
        ('week10', '第十周'),
        ('week11', '第十一周'),
        ('week12', '第十二周'),
        ('week13', '第十三周'),
        ('week14', '第十四周'),
        ('week15', '第十五周'),
        ('week16', '第十六周')
    )



    course_id = models.IntegerField(null=False, blank=False, default=12345, verbose_name=u'课程编号')
    course_name = models.CharField(null=False, blank=False, max_length=30, default="xx课程", verbose_name=u'课程名称')
    course_location = models.CharField(null=False, blank=False, max_length=20, default='地点未知', verbose_name=u'课程地点')
    course_point = models.IntegerField(null=False, blank=False, default=2, verbose_name=u'课程学分')
    course_length = models.IntegerField(null=False, blank=False, default=32, verbose_name=u'课程学时')
    course_startWeek = models.CharField(null=False, blank=False, choices=WEEK_CHOICE, max_length=6, default='week1', verbose_name=u'课程开始周')
    course_endWeek = models.CharField(null=False, blank=False, choices=WEEK_CHOICE, max_length=6, default='week16', verbose_name=u'课程结束周')
    course_time = models.ForeignKey(CourseTime, on_delete=models.CASCADE, verbose_name=u'上课时间(多选)')


    class Meta:
        verbose_name = u'课程信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.course_name

