# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-14 16:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prelaunch', '0003_auto_20170310_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
