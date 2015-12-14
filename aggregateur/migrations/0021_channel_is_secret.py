# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aggregateur', '0020_auto_20151022_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='is_secret',
            field=models.BooleanField(default=False, verbose_name='Secrète'),
        ),
    ]
