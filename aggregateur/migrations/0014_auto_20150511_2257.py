# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aggregateur', '0013_auto_20150503_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='channel',
            field=models.ForeignKey(blank=True, null=True, to='aggregateur.Channel'),
        ),
    ]
