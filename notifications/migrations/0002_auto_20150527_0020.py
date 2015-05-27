# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='non_lu',
        ),
        migrations.AddField(
            model_name='notification',
            name='lue',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='notification',
            name='vue',
            field=models.BooleanField(default=False),
        ),
    ]
