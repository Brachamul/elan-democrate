# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aggregateur', '0022_auto_20151104_0043'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='num_subscribers',
            field=models.PositiveIntegerField(editable=False, default=0),
        ),
    ]
