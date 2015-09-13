# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aggregateur', '0002_auto_20150904_0053'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='shareable',
            field=models.BooleanField(default=True),
        ),
    ]
