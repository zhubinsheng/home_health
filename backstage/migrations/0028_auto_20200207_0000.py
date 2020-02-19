# Generated by Django 3.0.3 on 2020-02-07 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backstage', '0027_auto_20200206_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowmoneyin',
            name='datetime',
            field=models.DateField(default='2020-02-07', verbose_name='日期'),
        ),
        migrations.AlterField(
            model_name='lendmoneyin',
            name='datetime',
            field=models.DateField(default='2020-02-07', verbose_name='日期'),
        ),
        migrations.AlterField(
            model_name='paymoneyin',
            name='datetime',
            field=models.DateField(default='2020-02-07', verbose_name='日期'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='birth',
            field=models.DateField(blank=True, default='2020-02-07', null=True, verbose_name='出生日期'),
        ),
    ]
