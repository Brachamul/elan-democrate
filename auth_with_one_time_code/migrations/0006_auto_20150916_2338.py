# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_with_one_time_code', '0005_auto_20150916_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credentials',
            name='code',
            field=models.CharField(default='7TM4JL', max_length=6),
        ),
        migrations.AlterField(
            model_name='emailconfirmationinstance',
            name='code',
            field=models.CharField(default='228016TNDS0B2FTZZ0RCVLXA99R0LX2F', max_length=32),
        ),
    ]
