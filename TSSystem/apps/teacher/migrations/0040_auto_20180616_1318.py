# Generated by Django 2.0.5 on 2018-06-16 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0039_auto_20180616_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='teacher_password',
            field=models.CharField(default='pbkdf2_sha256$100000$FvaIb9xcOUhx$cI4xGup6LDAlXEgMGKiv0X9WXBZAYU5Dd+M5XBxODuc=', max_length=100, verbose_name='教师账号密码'),
        ),
    ]
