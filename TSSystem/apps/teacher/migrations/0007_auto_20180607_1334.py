# Generated by Django 2.0.5 on 2018-06-07 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0006_auto_20180606_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='teacher_password',
            field=models.CharField(default='pbkdf2_sha256$100000$uKePxxEnUAkB$Mlcmbtun1OwV2h6e+XmVUVsS0aNeKz5LDz+KC1cTcoE=', max_length=100, verbose_name='教师账号密码'),
        ),
    ]