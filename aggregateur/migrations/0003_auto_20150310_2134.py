# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aggregateur', '0002_auto_20150308_2120'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tag',
            new_name='Channel',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='tags',
            new_name='channel',
        ),
    ]
