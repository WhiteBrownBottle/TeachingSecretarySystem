# Generated by Django 2.0.5 on 2018-06-14 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_arrangement', '0002_auto_20180614_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selection',
            name='course_classroom',
            field=models.IntegerField(blank=True, default=999, null=True, verbose_name='上课教室'),
        ),
    ]
