# Generated by Django 2.1.4 on 2018-12-31 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backstage', '0004_auto_20181231_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='birth',
            field=models.DateField(default='2018-12-31', verbose_name='出生日期'),
        ),
    ]
