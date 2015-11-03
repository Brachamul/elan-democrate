# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('aggregateur', '0021_channel_is_secret'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='description',
            field=models.CharField(verbose_name='Déscription', max_length=255),
        ),
        migrations.AlterField(
            model_name='channel',
            name='ignorers',
            field=models.ManyToManyField(verbose_name='Ignoreurs', related_name='ignored_channels', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AlterField(
            model_name='channel',
            name='moderators',
            field=models.ManyToManyField(verbose_name='Modérateurs', related_name='moderated_channels', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AlterField(
            model_name='channel',
            name='name',
            field=models.CharField(verbose_name='Nom', max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='channel',
            name='subscribers',
            field=models.ManyToManyField(verbose_name='Inscrits', related_name='subscribed_channels', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AlterField(
            model_name='channel',
            name='want_to_join',
            field=models.ManyToManyField(verbose_name='Veulent rejoindre', related_name='applied_to_channels', to=settings.AUTH_USER_MODEL, through='aggregateur.WantToJoinChannel', blank=True),
        ),
    ]
