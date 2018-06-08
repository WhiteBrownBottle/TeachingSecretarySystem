from django.db import models
from django.utils import timezone
import time
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


class Notification(models.Model):
    #Srtp消息通知

    notifi_id = models.IntegerField(default=123, unique=True, verbose_name=u'通知id')
    notifi_date = models.DateField(default=timezone.now, verbose_name=u'通知发布时间')
    notifi_title = models.CharField(blank=False, null=False, max_length=50, default='未命名消息通知', verbose_name=u'通知标题')
    notifi_content = models.TextField(blank=True, null=True, verbose_name=u'通知内容')

    class Meta:
        verbose_name = u'消息通知'
        verbose_name_plural = verbose_name


    def __str__(self):
        return '[%d: %s]' %(self.notifi_id, self.notifi_title)

    def save(self, *args, **kwargs):
        self.notifi_id = int(time.time())
        super(Notification, self).save(*args, **kwargs)



class NotifiFile(models.Model):
    #Srtp消息通知附件

    notifi_belong = models.ForeignKey(Notification, on_delete=models.CASCADE, verbose_name=u'所属通知')
    notifi_file_name = models.CharField(blank=True, null=True, max_length=100, default='暂未命名' , verbose_name=u'通知附件名称')
    notifi_file_url = models.FileField(blank=True, null=True, unique=True, upload_to='SrtpNotification/', default='', verbose_name=u'通知附件路径')

    class Meta:
        verbose_name = u'通知附件'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.notifi_file_name

    def save(self, *args, **kwargs):
        notifi_file_url = str(self.notifi_file_url)
        self.notifi_file_name = notifi_file_url
        super(NotifiFile, self).save(*args, **kwargs)