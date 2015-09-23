# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_with_one_time_code', '0008_auto_20150918_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credentials',
            name='code',
            field=models.CharField(max_length=6, default='4ZKLIQ'),
        ),
        migrations.AlterField(
            model_name='emailconfirmationinstance',
            name='code',
            field=models.CharField(max_length=32, default='0ARE6H58CWOYQ35RY4X1VICPV9OG9ZEA'),
        ),
    ]
