# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('aggregateur', '0003_auto_20150924_0136'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 24, 1, 49, 1, 408393), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='channel',
            name='slug',
            field=autoslug.fields.AutoSlugField(populate_from='name', editable=False, default='potato'),
            preserve_default=False,
        ),
    ]
