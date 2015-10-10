# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aggregateur', '0015_auto_20151008_0149'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-is_pinned', '-rank', '-date']},
        ),
        migrations.AddField(
            model_name='channel',
            name='only_mods_can_post',
            field=models.BooleanField(default=False, verbose_name='Seuls les modérateurs peuvent poster'),
        ),
        migrations.AddField(
            model_name='post',
            name='is_pinned',
            field=models.BooleanField(default=False, verbose_name='Maintenir en haut'),
        ),
    ]
