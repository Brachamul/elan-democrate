# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('beta', '0002_auto_20150926_1145'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='betacandidat',
            options={'ordering': ['-converted', '-date']},
        ),
        migrations.AddField(
            model_name='betacandidat',
            name='converted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='betacandidat',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 26, 12, 5, 20, 355942), auto_now_add=True),
            preserve_default=False,
        ),
    ]
