# Generated by Django 2.0.5 on 2018-06-03 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_auto_20180603_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_password',
            field=models.CharField(default='pbkdf2_sha256$100000$Oy2AoKspBjqD$4Bw/VN5N3TbjDXo7fjdbrv/3/IKuPFJgdtDLbyreBhs=', max_length=100, verbose_name='学生账号密码'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teacher_password',
            field=models.CharField(default='pbkdf2_sha256$100000$qhzmtvACucyZ$Ty/zthrdAmO3PNXIGiJ8db/IoSfcbe7VoGLx28iBVbk=', max_length=100, verbose_name='教师账号密码'),
        ),
    ]