# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aggregateur', '0008_lastranking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='channel',
            field=models.ForeignKey(to='aggregateur.Channel', null=True),
            preserve_default=True,
        ),
    ]
