# Generated by Django 2.0.5 on 2018-06-14 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0032_auto_20180614_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='teacher_password',
            field=models.CharField(default='pbkdf2_sha256$100000$863EcaqTLnSl$wnc+ftC2UCYOdQ6lRYGWPxQVpnPMSUg+dvon1ubh7ZI=', max_length=100, verbose_name='教师账号密码'),
        ),
    ]
