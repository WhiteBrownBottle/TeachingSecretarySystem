# Generated by Django 2.0.5 on 2018-06-07 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_auto_20180607_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_password',
            field=models.CharField(default='pbkdf2_sha256$100000$eMziDWrgKmag$U93RwGX8kzgpYkGsqd3FEflmTlYvCnFqnk4VNjsq0vo=', max_length=100, verbose_name='学生账号密码'),
        ),
    ]
