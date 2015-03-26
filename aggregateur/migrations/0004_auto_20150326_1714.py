# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aggregateur', '0003_auto_20150325_2226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='score',
            new_name='health',
        ),
    ]
