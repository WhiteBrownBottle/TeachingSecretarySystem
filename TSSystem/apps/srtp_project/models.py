from django.db import models
import datetime, time
import django.utils.timezone as timezone
from student.models import Student
from teacher.models import Teacher
from utils.customfilefield.storage import FileStorage

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

    STATUS_APPLY_CHOICE = (
        (True, '已申请'),
        (False, '未申请')
    )

    STATUS_CHECK_CHOICE = (
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
    project_appli_student = models.OneToOneField(Student, blank=True, null=True, on_delete=models.CASCADE, verbose_name='项目申请人')
    project_appli_name = models.CharField(max_length=100, blank=True, null=True, verbose_name=u'项目申请书名称')
    project_appli_url = models.CharField(max_length=100, blank=True, null=True, verbose_name=u'项目申请书路径')
    project_fund_appli = models.IntegerField(blank=False, null=False, default=3000, verbose_name=u'项目申请经费')
    project_fund_approv = models.IntegerField(blank=False, null=False, default=3000, verbose_name=u'项目批准经费')
    project_date_begin = models.DateField(default=timezone.now, verbose_name=u'项目立项日期')
    project_date_end = models.DateField(default=timezone.now, verbose_name=u'项目结束日期')
    project_period = models.CharField(null=False, blank=False, max_length=10, default='1年', verbose_name=u'项目周期')
    project_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='项目指导老师')
    project_member = models.CharField(null=True, blank=True, max_length=50, default="暂未填写", verbose_name='项目成员')
    project_check_status = models.BooleanField(blank=False, null=False, default=False, choices=STATUS_CHECK_CHOICE, verbose_name=u'项目审核状态')
    project_apply_status = models.BooleanField(blank=False, null=False, default=False, choices=STATUS_APPLY_CHOICE, verbose_name=u'项目申请状态')
    project_suggest_people_num = models.CharField(null=True, blank=True, max_length=50, default="暂未填写", verbose_name='人数建议')
    project_subject = models.CharField(null=True, blank=True, max_length=20, default="暂未填写", verbose_name='项目所属学科')


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


class Fund(models.Model):
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

    project_belong = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name=u'所属srtp项目')
    fund_name = models.CharField(null=True, blank=True, max_length=100, verbose_name=u'具体支出项目摘要')
    fund_type = models.CharField(null=False, blank=False, max_length=9, choices=FUND_TYPE_CHOICE, default='12', verbose_name=u'经费类别')
    fund_num = models.IntegerField(null=True, blank=True, verbose_name=u'经费支出金额')
    fund_date = models.DateField(default=timezone.now, verbose_name=u'经费支出日期')

    class Meta:
        verbose_name = u'SRTP项目经费管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '[%s: %d]' %(self.fund_type, self.fund_num)


class Result(models.Model):
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
    project_belong = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name=u'所属srtp项目')
    result_name = models.CharField(blank=False, null=False, max_length=50, default='未命名成果', verbose_name=u'项目成果名称')
    result_type = models.CharField(blank=False, null=False, max_length=8, default='7', choices=RESULT_TYPE_CHOICE, verbose_name=u'项目成果类型')
    result_date = models.DateField(default=timezone.now, verbose_name='项目成果日期')
    result_master = models.CharField(blank=False, null=False, max_length=20, default='未填写', verbose_name=u'项目成果所有人')
    result_file_name = models.CharField(blank=True, null=True, max_length=100, verbose_name=u'项目附件名称')
    result_file_url = models.CharField(blank=True, null=True, max_length=100, verbose_name=u'项目附件路径')

    class Meta:
        verbose_name = u'SRTP项目成果管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '[%s: %s]' % (self.result_name, self.result_master)


class AddFund(models.Model):
    #Srtp追加经费

    ADDFUND_CHECK_STATUS_CHOICE = (
        ('0', '未通过'),
        ('1', '通过'),
    )

    ADDFUND_ADD_STATUS_CHOICE = (
        ('0', '未添加'),
        ('1', '已添加'),
    )

    project_belong = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name=u'所属srtp项目')
    addfund_date = models.DateField(default=timezone.now, verbose_name=u'追加经费申请时间')
    addfund_num = models.IntegerField(null=True, blank=True, verbose_name=u'追加经费数目')
    addfund_reason = models.TextField(blank=True, null=True, verbose_name=u'追加经费理由')
    addfund_check_status = models.CharField(null=False, blank=False, max_length=1, default='0', choices=ADDFUND_CHECK_STATUS_CHOICE, verbose_name='追加经费审核状态')
    addfund_add_status = models.CharField(null=False, blank=False, editable=False, max_length=1, default='0', choices=ADDFUND_ADD_STATUS_CHOICE, verbose_name=u'追加经费添加状态')

    class Meta:
        verbose_name = u'SRTP项目追加经费'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '[%s : %d]' %(str(self.project_belong), self.addfund_num)


class MidTerm(models.Model):
    #中期检查

    CHECK_STATUS = (
        ('0', '未提交'),
        ('1', '审批中'),
        ('2', '已通过')
    )

    CHECK_POINT = (
        ('0', ''),
        ('1', '教师审核'),
        ('2', '管理员审核')
    )
    project_belong = models.OneToOneField(Project, on_delete=models.CASCADE, verbose_name=u'所属srtp项目')
    midterm_file_name = models.CharField(blank=True, null=True, max_length=100, verbose_name=u'文件名称')
    midterm_file_url = models.CharField(blank=True, null=True, max_length=100, verbose_name=u'文件路径')
    midterm_deadline_date = models.DateField(default=timezone.now, verbose_name=u'提交截止日期')
    midterm_check_status = models.CharField(blank=False, null=False, choices=CHECK_STATUS, max_length=1, default='0', verbose_name=u'审核状态')
    midterm_check_point = models.CharField(blank=False, null=False, choices=CHECK_POINT, max_length=1, default='0', verbose_name=u'审核节点')

    class Meta:
        verbose_name = u'SRTP项目中期检查'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '[%s: %s]' %(self.midterm_file_name, self.midterm_check_status)


class Conclusion(models.Model):
    #Srtp结题

    CHECK_STATUS = (
        ('0', '未提交'),
        ('1', '审批中'),
        ('2', '已通过')
    )

    CHECK_POINT = (
        ('0', ''),
        ('1', '教师审核'),
        ('2', '管理员审核')
    )
    project_belong = models.OneToOneField(Project, on_delete=models.CASCADE, verbose_name=u'所属srtp项目')
    conclusion_file_name = models.CharField(blank=True, null=True, max_length=100, verbose_name=u'文件名称')
    conclusion_file_url = models.CharField(blank=True, null=True, max_length=100, verbose_name=u'文件路径')
    conclusion_deadline_date = models.DateField(default=timezone.now, verbose_name=u'提交截止日期')
    conclusion_check_status = models.CharField(blank=False, null=False, choices=CHECK_STATUS, max_length=1, default='0',
                                            verbose_name=u'审核状态')
    conclusion_check_point = models.CharField(blank=False, null=False, choices=CHECK_POINT, max_length=1, default='0',
                                           verbose_name=u'审核节点')

    class Meta:
        verbose_name = u'SRTP项目结题检查'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '[%s: %s]' %(self.conclusion_file_name, self.conclusion_check_status)


class Notification(models.Model):
    #Srtp消息通知

    notifi_id = models.IntegerField(default=int(time.time()), unique=True, verbose_name=u'通知id')
    notifi_date = models.DateField(default=timezone.now, verbose_name=u'通知发布时间')
    notifi_title = models.CharField(blank=False, null=False, max_length=50, default='未命名消息通知', verbose_name=u'通知标题')
    notifi_content = models.TextField(blank=True, null=True, verbose_name=u'通知内容')

    class Meta:
        verbose_name = u'SRTP项目消息通知'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '[%d: %s]' %(self.notifi_id, self.notifi_title)



class NotifiFile(models.Model):
    #Srtp消息通知附件

    notifi_belong = models.ForeignKey(Notification, on_delete=models.CASCADE, verbose_name=u'所属通知')
    notifi_file_name = models.CharField(blank=True, null=True, max_length=100, default='暂未命名' , verbose_name=u'通知附件名称')
    notifi_file_url = models.FileField(blank=True, null=True, unique=True, upload_to='SrtpNotification/', default='', verbose_name=u'通知附件路径')

    class Meta:
        verbose_name = u'SRTP项目通知附件'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.notifi_file_name

    def save(self, *args, **kwargs):
        notifi_file_url = str(self.notifi_file_url)
        self.notifi_file_name = notifi_file_url
        super(NotifiFile, self).save(*args, **kwargs)





















