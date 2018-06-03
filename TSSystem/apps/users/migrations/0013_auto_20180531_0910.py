# Generated by Django 2.0.5 on 2018-05-31 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20180531_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_password',
            field=models.CharField(default='pbkdf2_sha256$100000$t8L2ac0P3jNY$OIlrMd1XBj38I7RoImDy53N3n/7LhRC0bOH0KrOcWTA=', max_length=100, verbose_name='学生账号密码'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teacher_password',
            field=models.CharField(default='pbkdf2_sha256$100000$5aaqIt29pvvU$vgImuoid5lyra7Fbk1GX/gX8C2en/Zaa0S5xAwmOefw=', max_length=100, verbose_name='教师账号密码'),
        ),
    ]