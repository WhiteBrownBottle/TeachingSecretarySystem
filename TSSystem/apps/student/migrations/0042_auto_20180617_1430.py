# Generated by Django 2.0.5 on 2018-06-17 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0041_auto_20180616_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_password',
            field=models.CharField(default='pbkdf2_sha256$100000$LltjeysPXLHW$qPLc0VL+kc2//2glwaarvMA7UoA/nWZksl2K/mX848s=', max_length=100, verbose_name='学生账号密码'),
        ),
    ]
