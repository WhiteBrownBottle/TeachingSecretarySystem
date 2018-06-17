# Generated by Django 2.0.5 on 2018-06-17 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_arrangement', '0010_auto_20180616_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='is_arranged',
            field=models.BooleanField(choices=[(True, '本课已排'), (False, '本课未排')], default=True, verbose_name='是否排课'),
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