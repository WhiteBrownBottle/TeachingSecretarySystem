# Generated by Django 2.0.5 on 2018-06-14 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0035_auto_20180614_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='teacher_password',
            field=models.CharField(default='pbkdf2_sha256$100000$sg8YI4HaztBo$GEe21ApynPCQXhkRmdYIy/fhqg4sDCdRqaYYNtBHzvI=', max_length=100, verbose_name='教师账号密码'),
        ),
    ]