# Generated by Django 2.0.5 on 2018-06-14 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0031_auto_20180614_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='teacher_password',
            field=models.CharField(default='pbkdf2_sha256$100000$z5U6eHcndjNM$kusddJNbxy0VgQTYsqnVnpU/rmZ7nUz4pmZOFMM8B7A=', max_length=100, verbose_name='教师账号密码'),
        ),
    ]
