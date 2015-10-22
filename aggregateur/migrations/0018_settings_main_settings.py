# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aggregateur', '0017_settings'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='main_settings',
            field=models.BooleanField(default=True, unique=True),
        ),
    ]
