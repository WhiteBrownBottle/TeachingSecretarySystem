from django.db import models
from datetime import date
from main_platform.models import Grade, Class
from django.contrib.auth.models import AbstractUser



class Student(models.Model):

    # 自定义性别选项规则
    GENDER_CHOICES = (
        ('male', '男'),
        ('female', '女'),
    )

    s_id = models.IntegerField(null=False, blank=False, default=12345678, verbose_name=u'学号')
    s_name = models.CharField(null=False, blank=False, max_length=20, default='某某学生',verbose_name=u'学生姓名')
    s_gender = models.CharField(null=False, blank=False, max_length=6, choices=GENDER_CHOICES, default='male', verbose_name=u'学生性别')
    s_birthday = models.DateField(null=True, blank=True, auto_now=True, verbose_name=u'出生年龄')
    s_class_belong = models.ForeignKey(Class, on_delete=models.CASCADE, verbose_name=u'所属班级')

    class Meta:
        verbose_name = u'学生信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.s_name


class Teacher(models.Model):

    #自定义性别选项规则
    GENDER_CHOICES = (
        ('male', '男'),
        ('female', '女'),
    )

    t_id = models.IntegerField(null=False, blank=False, default=12345, verbose_name=u'教师编号')
    t_name = models.CharField(null=False,blank=False, max_length=20, default='某某教师', verbose_name=u'教师姓名')
    t_gender = models.CharField(null=False, blank=False, max_length=6, choices=GENDER_CHOICES, default='male', verbose_name=u'教师性别')
    t_phone = models.IntegerField(null=False, blank=False, default=11111111111, verbose_name=u'教师电话号码')
    t_title = models.CharField(null=False, blank=False, max_length=20, default='教师', verbose_name=u'教师职称')

    class Meta:
        verbose_name = u'教师信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.t_name




