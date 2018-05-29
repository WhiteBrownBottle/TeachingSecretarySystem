from django.db import models
from datetime import date
from main_platform.models import Grade, Class
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password, check_password



class Student(models.Model):

    # 自定义性别选项规则
    GENDER_CHOICES = (
        ('male', '男'),
        ('female', '女'),
    )

    student_id = models.IntegerField(null=False, blank=False, default=12345678, unique=True, verbose_name=u'学号')
    student_name = models.CharField(null=False, blank=False, max_length=20, default='某某学生',verbose_name=u'学生姓名')
    student_password = models.CharField(null=False, blank=False, max_length=100, default=make_password('1111'), verbose_name=u'学生账号密码')
    student_gender = models.CharField(null=False, blank=False, max_length=6, choices=GENDER_CHOICES, default='male', verbose_name=u'学生性别')
    student_birthday = models.DateField(null=True, blank=True, auto_now=True, verbose_name=u'出生年龄')
    student_class_belong = models.ForeignKey(Class, on_delete=models.CASCADE, verbose_name=u'所属班级')

    class Meta:
        verbose_name = u'学生信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.student_name


class Teacher(models.Model):

    #自定义性别选项规则
    GENDER_CHOICES = (
        ('male', '男'),
        ('female', '女'),
    )

    teacher_id = models.IntegerField(null=False, blank=False, default=12345, unique=True, verbose_name=u'教师编号')
    teacher_password = models.CharField(null=False, blank=False, max_length=100, default=make_password('1111'), verbose_name=u'教师账号密码')
    teacher_name = models.CharField(null=False,blank=False, max_length=20, default='某某教师', verbose_name=u'教师姓名')
    teacher_gender = models.CharField(null=False, blank=False, max_length=6, choices=GENDER_CHOICES, default='male', verbose_name=u'教师性别')
    teacher_phone = models.IntegerField(null=False, blank=False, default=11111111111, verbose_name=u'教师电话号码')
    teacher_title = models.CharField(null=False, blank=False, max_length=20, default='教师', verbose_name=u'教师职称')

    class Meta:
        verbose_name = u'教师信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.teacher_name




