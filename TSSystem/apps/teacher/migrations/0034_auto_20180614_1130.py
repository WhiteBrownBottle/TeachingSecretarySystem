# Generated by Django 2.0.5 on 2018-06-14 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0033_auto_20180614_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='teacher_password',
            field=models.CharField(default='pbkdf2_sha256$100000$aI0LlE6OTyqp$lXtAtYg/7xRzgcei4Li0LYjZug1PrwiHqEBNvI7EUi4=', max_length=100, verbose_name='教师账号密码'),
        ),
    ]