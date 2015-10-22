# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aggregateur', '0010_auto_20151004_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='is_private',
            field=models.BooleanField(default=False),
        ),
    ]
