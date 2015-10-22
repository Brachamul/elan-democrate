# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_with_one_time_code', '0010_auto_20150922_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credentials',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
