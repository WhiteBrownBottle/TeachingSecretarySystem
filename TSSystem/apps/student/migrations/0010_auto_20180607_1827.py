# Generated by Django 2.0.5 on 2018-06-07 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_auto_20180607_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_password',
            field=models.CharField(default='pbkdf2_sha256$100000$iq3NB2BHLCRA$xxk/coXT3D/SrTH2O9Dm0YP2WMuKTr8WMV4xBi/HNLk=', max_length=100, verbose_name='学生账号密码'),
        ),
    ]