from django.db import models
import datetime, time
import django.utils.timezone as timezone
from student.models import Student
from teacher.models import Teacher
from utils.customfilefield.storage import FileStorage
# Create your models here.

class EduProject(models.Model):
    #教改/教研/教材项目数据模型
    TYPE_CHOICE = (
        ('zd', '重点'),
        ('zdzx', '重点专项'),
        ('ms', '面上'),
    )


    eduproject_id = models.AutoField(primary_key=True, unique=True, verbose_name=u'项目编号')
    eduproject_name = models.CharField(max_length=20, blank=False, null=False, default='xx项目', verbose_name=u'项目名称')
    eduproject_belong_unit = models.CharField(max_length=20, blank=False, null=False, default='xx单位', verbose_name=u'申请单位')
    eduproject_fund_appli = models.IntegerField(blank=False, null=False, default=3000, verbose_name=u'项目申请经费')
    eduproject_type = models.CharField(max_length=2, blank=False, null=False, choices=TYPE_CHOICE, default='zd', verbose_name=u'项目类别')
    eduproject_date_begin = models.DateField(default=timezone.now, verbose_name=u'起始日期')
    eduproject_date_end = models.DateField(default=timezone.now, verbose_name=u'结束日期')
    eduproject_person_in_charge = models.ForeignKey(Teacher, blank=True, null=True, on_delete=models.CASCADE, verbose_name='项目负责人')
    eduproject_appli_name = models.CharField(max_length=100, blank=True, null=True, verbose_name=u'项目申请书名称')
    eduproject_appli_url = models.CharField(max_length=100, blank=True, null=True, verbose_name=u'项目申请书路径')
    eduproject_member = models.CharField(null=True, blank=True, max_length=50, default="暂未填写", verbose_name='项目成员')
    eduproject_select_result = models.CharField(null=True, blank=True, max_length=20, default="暂无", verbose_name='项目评选结果')

    class Meta:
        verbose_name = u'教改/教研/教材项目信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '[%d:%s]' %(self.eduproject_id, self.eduproject_name)


class EduMidTerm(models.Model):
    #中期检查

    CHECK_STATUS = (
        ('0', '未提交'),
        ('1', '审批中'),
        ('2', '已通过')
    )

    eduproject_belong = models.OneToOneField(EduProject, on_delete=models.CASCADE, verbose_name=u'所属教改/教研/教材项目')
    edumidterm_file_name = models.CharField(blank=True, null=True, max_length=100, verbose_name=u'文件名称')
    edumidterm_file_url = models.CharField(blank=True, null=True, max_length=100, verbose_name=u'文件路径')
    edumidterm_deadline_date = models.DateField(default=timezone.now, verbose_name=u'提交截止日期')
    edumidterm_check_status = models.CharField(blank=False, null=False, choices=CHECK_STATUS, max_length=1, default='0', verbose_name=u'审核状态')

    class Meta:
        verbose_name = u'教改/教研/教材项目中期检查'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '[%s: %s]' %(self.edumidterm_file_name, self.edumidterm_check_status)

class EduConclusion(models.Model):
    #项目结题

    CHECK_STATUS = (
        ('0', '未提交'),
        ('1', '审批中'),
        ('2', '已通过')
    )

    eduproject_belong = models.OneToOneField(EduProject, on_delete=models.CASCADE, verbose_name=u'所属教改/教研/教材项目')
    educonclusion_file_name = models.CharField(blank=True, null=True, max_length=100, verbose_name=u'文件名称')
    educonclusion_file_url = models.CharField(blank=True, null=True, max_length=100, verbose_name=u'文件路径')
    educonclusion_deadline_date = models.DateField(default=timezone.now, verbose_name=u'提交截止日期')
    educonclusion_check_status = models.CharField(blank=False, null=False, choices=CHECK_STATUS, max_length=1, default='0',
                                            verbose_name=u'审核状态')

    class Meta:
        verbose_name = u'教改/教研/教材项目结题'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '[%s: %s]' %(self.educonclusion_file_name, self.educonclusion_check_status)


class EduFund(models.Model):
    #项目经费

    FUND_TYPE_CHOICE = (
        ('1', '差旅费'),
        ('2', '实验费'),
        ('3', '资料费'),
        ('4', '实验耗材费'),
        ('5', '计算机小型存储设备费'),
        ('6', '邮寄费'),
        ('7', '论文版面费'),
        ('8', '成果鉴定费'),
        ('9', '专利申请费'),
        ('10', '文件检索费'),
        ('11', '办公费'),
        ('12', '其他费用')
    )

    eduproject_belong = models.ForeignKey(EduProject, on_delete=models.CASCADE, verbose_name=u'所属教改/教研/教材项目')
    edufund_name = models.CharField(null=True, blank=True, max_length=100, verbose_name=u'具体支出项目摘要')
    edufund_type = models.CharField(null=False, blank=False, max_length=9, choices=FUND_TYPE_CHOICE, default='12', verbose_name=u'经费类别')
    edufund_num = models.IntegerField(null=True, blank=True, verbose_name=u'经费支出金额')
    edufund_date = models.DateField(default=timezone.now, verbose_name=u'经费支出日期')

    class Meta:
        verbose_name = u'经费管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '[%s: %d]' %(self.edufund_type, self.edufund_num)


class EduResult(models.Model):
    #项目成果

    RESULT_TYPE_CHOICE = (
        ('1', '著作/著作权'),
        ('2', '论文'),
        ('3', '专利'),
        ('4', '实物'),
        ('5', '软件/图纸/设计'),
        ('6', '获奖证书'),
        ('7', '其他')
    )
    eduproject_belong = models.ForeignKey(EduProject, on_delete=models.CASCADE, verbose_name=u'所属srtp项目')
    eduresult_name = models.CharField(blank=False, null=False, max_length=50, default='未命名成果', verbose_name=u'项目成果名称')
    eduresult_type = models.CharField(blank=False, null=False, max_length=8, default='7', choices=RESULT_TYPE_CHOICE, verbose_name=u'项目成果类型')
    eduresult_date = models.DateField(default=timezone.now, verbose_name='项目成果日期')
    eduresult_master = models.CharField(blank=False, null=False, max_length=20, default='未填写', verbose_name=u'项目成果所有人')
    eduresult_file_name = models.CharField(blank=True, null=True, max_length=100, verbose_name=u'项目附件名称')
    eduresult_file_url = models.CharField(blank=True, null=True, max_length=100, verbose_name=u'项目附件路径')

    class Meta:
        verbose_name = u'成果管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '[%s: %s]' % (self.eduresult_name, self.eduresult_master)