# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aggregateur', '0012_auto_20150503_2126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentvote',
            name='post',
        ),
        migrations.AddField(
            model_name='commentvote',
            name='comment',
            field=models.ForeignKey(default=1, to='aggregateur.Comment'),
            preserve_default=False,
        ),
    ]
