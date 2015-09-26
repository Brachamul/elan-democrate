# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aggregateur', '0002_auto_20150916_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='description',
            field=models.CharField(null=True, blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='channel',
            name='ignorers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='ignored_channels'),
        ),
        migrations.AddField(
            model_name='channel',
            name='is_default',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='channel',
            name='moderators',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='moderated_channels'),
        ),
        migrations.AddField(
            model_name='channel',
            name='subscribers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='subscribed_channels'),
        ),
    ]
