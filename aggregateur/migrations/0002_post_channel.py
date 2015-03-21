# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aggregateur', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='channel',
            field=models.ForeignKey(default=1, to='aggregateur.Channel'),
            preserve_default=False,
        ),
    ]
