# Generated by Django 2.1.4 on 2018-12-31 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backstage', '0013_auto_20181231_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='birth',
            field=models.DateField(verbose_name='出生日期'),
        ),
    ]