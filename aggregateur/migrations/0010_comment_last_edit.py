# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('aggregateur', '0009_auto_20150425_0032'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='last_edit',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 26, 20, 4, 13, 866897), auto_now=True),
            preserve_default=False,
        ),
    ]
