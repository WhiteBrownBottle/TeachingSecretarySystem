# Generated by Django 2.0.5 on 2018-06-07 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0017_auto_20180607_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_password',
            field=models.CharField(default='pbkdf2_sha256$100000$60wGzGkgepff$+FPdVTqtWJsJKKhKEzdL0DlBHZnijLIkrgY6ZRc+iUI=', max_length=100, verbose_name='学生账号密码'),
        ),
    ]
