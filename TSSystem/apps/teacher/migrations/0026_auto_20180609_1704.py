# Generated by Django 2.0.5 on 2018-06-09 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0025_auto_20180609_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='teacher_password',
            field=models.CharField(default='pbkdf2_sha256$100000$Osv2Ag79rDiB$ZP9ZaBz9lIBhqM72QU6+r1hQIFYBRV0wFJqI0hesxTI=', max_length=100, verbose_name='教师账号密码'),
        ),
    ]