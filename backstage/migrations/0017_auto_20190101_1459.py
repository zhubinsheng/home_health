# Generated by Django 2.1.4 on 2019-01-01 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backstage', '0016_auto_20181231_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='birth',
            field=models.DateField(blank=True, default='2019-01-01', null=True, verbose_name='出生日期'),
        ),
    ]
