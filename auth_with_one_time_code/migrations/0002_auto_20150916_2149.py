# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_with_one_time_code', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credentials',
            name='code',
            field=models.CharField(max_length=6, default='TKV5QX'),
        ),
        migrations.AlterField(
            model_name='emailconfirmationinstance',
            name='code',
            field=models.CharField(max_length=32, default='XMUTWW39BLFVGE6XB1IMS11K4ANDS85E'),
        ),
    ]
