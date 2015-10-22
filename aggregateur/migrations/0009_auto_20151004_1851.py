# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('aggregateur', '0008_auto_20150926_0349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='ignorers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True, related_name='ignored_channels'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='illustration',
            field=models.URLField(default='http://localhost:8000/static/images/default_channel_illustration.png'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='moderators',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True, related_name='moderated_channels'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=True, populate_from='name', unique=True),
        ),
        migrations.AlterField(
            model_name='channel',
            name='subscribers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True, related_name='subscribed_channels'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=autoslug.fields.AutoSlugField(unique_with=('date__year',), editable=False, populate_from='title'),
        ),
    ]
