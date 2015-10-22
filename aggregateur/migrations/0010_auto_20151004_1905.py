# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aggregateur', '0009_auto_20151004_1851'),
    ]

    operations = [
        migrations.RenameField(
            model_name='channel',
            old_name='official',
            new_name='is_official',
        ),
    ]
