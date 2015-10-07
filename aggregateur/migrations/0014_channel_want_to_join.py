# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aggregateur', '0013_auto_20151006_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='want_to_join',
            field=models.ManyToManyField(related_name='applied_to_channels', through='aggregateur.WantToJoinChannel', blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
