from django.db import models

# Create your models here.


class Grade(models.Model):

    GRADE_CHOICE = (
        ('Grade_one', '大一'),
        ('Grade_two', '大二'),
        ('Grade_three', '大三'),
        ('Grade_four', '大四'),
    )

    grade_name = models.CharField(null=False, blank=False, default='Grade_one', max_length=11, unique=True, choices=GRADE_CHOICE, verbose_name=u'年级名')

    class Meta:
        verbose_name = u'年级信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.get_grade_name_display()


class Class(models.Model):

    grade_belong = models.ForeignKey(Grade, on_delete=models.CASCADE, verbose_name=u'所属年级')
    class_name = models.CharField(null=False, blank=False, max_length=20, default='未选班级', unique=True, verbose_name=u'班级名')

    class Meta:
        verbose_name = u'班级信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.class_name