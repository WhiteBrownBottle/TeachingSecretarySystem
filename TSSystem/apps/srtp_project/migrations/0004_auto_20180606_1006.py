# Generated by Django 2.0.5 on 2018-06-06 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srtp_project', '0003_notification_notififile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='project_status',
            new_name='project_check_status',
        ),
        migrations.AddField(
            model_name='project',
            name='project_apply_status',
            field=models.BooleanField(choices=[(True, '已申请'), (False, '未申请')], default=False, verbose_name='项目申请状态'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='notifi_id',
            field=models.IntegerField(default=1528250757, verbose_name='通知id'),
        ),
    ]
