# Generated by Django 2.0.5 on 2018-06-06 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0005_auto_20180606_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='teacher_password',
            field=models.CharField(default='pbkdf2_sha256$100000$LzXqfb3j8Krr$+7eQuyo5DrYyAcC8d6W8IWwGgzrrGPQwDKCSHpyz3cg=', max_length=100, verbose_name='教师账号密码'),
        ),
    ]