# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aggregateur', '0002_post_channel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_type',
            new_name='format',
        ),
    ]
