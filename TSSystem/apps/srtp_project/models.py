from django.db import models
import datetime
import django.utils.timezone as timezone
from users.models import Teacher, Student
# Create your models here.

class Project(models.Model):
    #srtp项目数据模型
    TYPE_CHOICE = (
        ('cx', '创新'),
        ('cy', '创业'),
    )

    RANK_CHOICE = (
        ('1', '一级'),
        ('2', '二级'),
        ('3', '三级'),
        ('4', '四级'),
        ('5', '五级'),
    )

    DEPART_CHOICE = (
        ('tm', '土木与资源工程学院'),
        ('yj', '冶金与生态工程学院'),
        ('cl', '材料科学与工程学院'),
        ('jx', '机械工程学院'),
        ('nh', '能源与环境工程学院'),
        ('zdh', '自动化学院'),
        ('jt', '计算机与通信工程学院'),
        ('sl', '数理学院'),
        ('hs', '化学与生物工程学院'),
        ('jg', '东凌经济管理学院'),
        ('wf', '文法学院'),
        ('mks', '马克思主义学院'),
        ('wgy', '外国语学院'),
        ('gg', '高等工程师学院')
    )

    STATUS_CHOICE = (
        (True, '通过'),
        (False, '未通过')
    )



    project_id = models.AutoField(primary_key=True, unique=True, verbose_name=u'项目编号')
    project_name = models.CharField(max_length=20, blank=False, null=False, default='xx项目', verbose_name=u'项目名称')
    project_type = models.CharField(max_length=2, blank=False, null=False, choices=TYPE_CHOICE, default='cx', verbose_name=u'项目类型')
    project_rank = models.CharField(max_length=1, blank=False, null=False, choices=RANK_CHOICE, default='1', verbose_name=u'项目等级')
    project_intro = models.CharField(max_length=1000, blank=True, verbose_name=u'项目简介')
    project_depart = models.CharField(max_length=3, blank=False, null=False, choices=DEPART_CHOICE, default='jt', verbose_name=u'项目所属学院')
    project_plan = models.CharField(max_length=10, blank=True, null=False, default="%d年创新计划" % (datetime.datetime.now().year), verbose_name=u'项目所属创新计划')
    project_form = models.CharField(max_length=40, blank=False, null=False, default='实体', verbose_name=u'项目成果形式')
    project_appli_student = models.OneToOneField(Student, on_delete=models.CASCADE, verbose_name='项目申请人')
    project_appli_name = models.CharField(max_length=100, blank=True, null=True, verbose_name=u'项目申请书名称')
    project_appli_url = models.CharField(max_length=100, blank=True, null=True, verbose_name=u'项目申请书路径')
    project_fund_appli = models.IntegerField(blank=False, null=False, default=3000, verbose_name=u'项目申请经费')
    project_fund_approv = models.IntegerField(blank=False, null=False, default=3000, verbose_name=u'项目批准经费')
    project_date_begin = models.DateField(default=timezone.now, verbose_name=u'项目立项日期')
    project_date_end = models.DateField(default=timezone.now, verbose_name=u'项目结束日期')
    project_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='项目指导老师')
    project_member = models.CharField(null=True, blank=True, max_length=50, default="暂未填写", verbose_name='项目成员')
    project_status = models.BooleanField(blank=False, null=False, default=False, choices=STATUS_CHOICE, verbose_name=u'项目审核状态')

    class Meta:
        verbose_name = u'SRTP项目信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '[%d:%s]' %(self.project_id, self.project_name)


class Schedule(models.Model):
    #项目进度
    project_belong = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name=u'所属srtp项目')
    schedule_date = models.DateField(default=timezone.now, verbose_name=u'记录时间')
    schedule_num = models.IntegerField(blank=False, null=False, default=1, verbose_name=u'项目进度')
    schedule_detail = models.TextField(blank=False, null=False, default='缺少说明，请补充', verbose_name=u'项目进展说明')

    class Meta:
        verbose_name = u'SRTP项目进度'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.schedule_detail






