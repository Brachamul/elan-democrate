# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aggregateur', '0014_channel_want_to_join'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='is_default',
            field=models.BooleanField(default=False, verbose_name='Par défaut'),
        ),
    ]
