# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('aggregateur', '0005_auto_20150924_0200'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='illustration',
            field=models.URLField(default='/static/images/default_channel_illustration.png'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='slug',
            field=autoslug.fields.AutoSlugField(max_length=255, editable=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=autoslug.fields.AutoSlugField(max_length=255, editable=False),
        ),
    ]
