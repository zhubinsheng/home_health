# Generated by Django 2.1.4 on 2018-12-31 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backstage', '0012_auto_20181231_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='birth',
            field=models.DateField(auto_now_add=True, verbose_name='出生日期'),
        ),
    ]
