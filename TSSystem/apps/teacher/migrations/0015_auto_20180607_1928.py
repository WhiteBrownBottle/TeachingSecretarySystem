# Generated by Django 2.0.5 on 2018-06-07 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0014_auto_20180607_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='teacher_password',
            field=models.CharField(default='pbkdf2_sha256$100000$wDPWuXLzQgO9$ivMHB/M4ckrfTv8v8xbCIgTavtz1EKnnlmWSdCfzXI4=', max_length=100, verbose_name='教师账号密码'),
        ),
    ]