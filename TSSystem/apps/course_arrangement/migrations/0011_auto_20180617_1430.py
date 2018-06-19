# Generated by Django 2.0.5 on 2018-06-17 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_arrangement', '0010_auto_20180616_1326'),
    ]

    operations = [
        migrations.CreateModel(
            name='GetTeacherCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_id', models.IntegerField(default=0, unique=True, verbose_name='所查询的教师编号')),
            ],
            options={
                'verbose_name': '所查询的教师编号',
                'verbose_name_plural': '所查询的教师编号',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='is_arranged',
            field=models.BooleanField(choices=[(True, '本课已排'), (False, '本课未排')], default=False, verbose_name='是否排课'),
        ),
        migrations.AlterField(
            model_name='selection',
            name='course_time',
            field=models.IntegerField(choices=[(1, '2'), (2, '3'), (3, '4'), (4, '5'), (5, '6'), (6, '1')], default=1, verbose_name='课程时间'),
        ),
        migrations.AlterField(
            model_name='selection',
            name='course_weekday',
            field=models.IntegerField(choices=[(1, '2'), (2, '3'), (3, '4'), (4, '5'), (5, '1')], default=1, verbose_name='课程上课日'),
        ),
    ]