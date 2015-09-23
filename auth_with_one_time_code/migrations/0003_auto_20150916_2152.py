# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_with_one_time_code', '0002_auto_20150916_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credentials',
            name='code',
            field=models.CharField(max_length=6, default='93SWJV'),
        ),
        migrations.AlterField(
            model_name='emailconfirmationinstance',
            name='code',
            field=models.CharField(max_length=32, default='UV39UDHWHWRAJJWL2S6LM6SBOBO5J2NQ'),
        ),
    ]
