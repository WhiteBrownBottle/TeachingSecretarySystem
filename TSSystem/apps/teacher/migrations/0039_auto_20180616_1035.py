# Generated by Django 2.0.5 on 2018-06-16 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0038_auto_20180614_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='teacher_password',
            field=models.CharField(default='pbkdf2_sha256$100000$91XDU2moi370$qNSxJUN6GkFQVONt4LGeyn4cC7wPet4TVV71uyrWITo=', max_length=100, verbose_name='教师账号密码'),
        ),
    ]
