# Generated by Django 2.0.5 on 2018-06-05 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_password',
            field=models.CharField(default='pbkdf2_sha256$100000$IWQkFCJWgvrE$7gSOIz2WDfHAO8OVclhaJF4Cbry3d4BSlr1/FQXfI4U=', max_length=100, verbose_name='学生账号密码'),
        ),
    ]