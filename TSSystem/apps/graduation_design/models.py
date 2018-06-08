from django.db import models
from django.utils import timezone
from student.models import Student
from teacher.models import Teacher

# Create your models here.


class ModelFile(models.Model):
    """
    文档模板
    """

    file_name = models.CharField(blank=True, null=True, max_length=100, default='暂未命名' , verbose_name=u'文件名称')
    file_url = models.FileField(blank=True, null=True, unique=True, upload_to='GradModelfile/', default='', verbose_name=u'文件路径')
    file_date = models.DateField(default=timezone.now, verbose_name=u'发布日期')

    class Meta:
        verbose_name = u'文档模板'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.file_name

    def save(self, *args, **kwargs):
        file_url = str(self.file_url)
        self.file_name = file_url
        super(ModelFile, self).save(*args, **kwargs)


class OpeningReport(models.Model):
    """
    开题报告
    """
    file_name = models.CharField(blank=True, null=True, max_length=100, default='暂未命名' , verbose_name=u'文件名称')
    file_url = models.CharField(blank=True, null=True, max_length=100, verbose_name=u'文件路径')
    file_date = models.DateField(default=timezone.now, verbose_name=u'上传日期')
    student_belong = models.OneToOneField(Student, blank=True, null=True, on_delete=models.CASCADE, verbose_name=u'创作学生')
    teacher_to = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name=u'指导老师')

    class Meta:
        verbose_name = u'开题报告'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '[%s: %s]' % (self.student_belong, self.file_name)


class MidtermReport(models.Model):
    """
    中期报告
    """
    file_name = models.CharField(blank=True, null=True, max_length=100, default='暂未命名', verbose_name=u'文档名称')
    file_url = models.CharField(blank=True, null=True, max_length=100, verbose_name=u'文件路径')
    file_date = models.DateField(default=timezone.now, verbose_name=u'上传日期')
    student_belong = models.OneToOneField(Student, blank=True, null=True, on_delete=models.CASCADE, verbose_name=u'创作学生')
    teacher_to = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name=u'指导老师')

    class Meta:
        verbose_name = u'中期报告'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '[%s: %s]' % (self.student_belong, self.file_name)


class Dissertation(models.Model):
    """
    毕业论文
    """

    file_name = models.CharField(blank=True, null=True, max_length=100, default='暂未命名', verbose_name=u'文档名称')
    file_url = models.CharField(blank=True, null=True, max_length=100, verbose_name=u'文件路径')
    file_date = models.DateField(default=timezone.now, verbose_name=u'上传日期')
    student_belong = models.OneToOneField(Student, on_delete=models.CASCADE, verbose_name=u'创作学生')
    teacher_to = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name=u'指导老师')

    class Meta:
        verbose_name = u'毕业论文'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '[%s: %s]' % (self.student_belong, self.file_name)











