from django.db import models
from datetime import date
import django.utils.timezone as timezone
from main_platform.models import Grade, Class
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password, check_password
# Create your models here.

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
    teacher_email = models.CharField(null=True, blank=True, unique=True, max_length=50, verbose_name=u'教师邮箱')
    teacher_title = models.CharField(null=False, blank=False, max_length=20, default='教师', verbose_name=u'教师职称')
    teacher_birth_date = models.DateField(default=timezone.now, verbose_name=u'出生日期')
    teacher_major = models.CharField(null=False, blank=False, max_length=20, default='暂未填写', verbose_name=u'教师专业')
    teacher_duty = models.CharField(null=False, blank=False, max_length=20, default='暂未填写', verbose_name=u'教师职务')

    class Meta:
        verbose_name = u'教师信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.teacher_name