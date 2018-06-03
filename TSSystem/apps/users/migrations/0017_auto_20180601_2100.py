# Generated by Django 2.0.5 on 2018-06-01 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20180601_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='teacher_email',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='教师邮箱'),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_password',
            field=models.CharField(default='pbkdf2_sha256$100000$WaJXiyiK6m1y$Q+esV8Sr7ehyfOJpIyfJMp6M4GirvYFv361MOfyAGpw=', max_length=100, verbose_name='学生账号密码'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teacher_password',
            field=models.CharField(default='pbkdf2_sha256$100000$JJy3DXItAN96$PuNpm3yMrwL21PPwTwNPj4f/+4nBvRNf36XgnVUrzV4=', max_length=100, verbose_name='教师账号密码'),
        ),
    ]