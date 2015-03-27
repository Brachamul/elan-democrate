# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aggregateur', '0004_auto_20150326_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='rank',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
