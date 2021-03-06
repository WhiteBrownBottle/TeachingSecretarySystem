# Generated by Django 2.0.5 on 2018-06-08 09:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('graduation_design', '0002_auto_20180607_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelfile',
            name='file_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='发布日期'),
        ),
        migrations.AlterField(
            model_name='modelfile',
            name='file_url',
            field=models.FileField(blank=True, default='', null=True, unique=True, upload_to='GradModelfile/', verbose_name='文件路径'),
        ),
    ]
