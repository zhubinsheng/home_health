# Generated by Django 2.1.4 on 2018-12-31 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backstage', '0009_auto_20181231_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='birth',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='出生日期'),
        ),
    ]
