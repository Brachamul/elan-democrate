# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aggregateur', '0011_channel_is_private'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='want_to_join',
            field=models.ManyToManyField(blank=True, related_name='applied_to_channels', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='channel',
            name='is_default',
            field=models.BooleanField(default=False, verbose_name='Par défaut"'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='is_official',
            field=models.BooleanField(default=False, verbose_name='Officielle'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='is_private',
            field=models.BooleanField(default=False, verbose_name='Privée'),
        ),
    ]
