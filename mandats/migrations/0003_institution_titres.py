# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mandats', '0002_auto_20150705_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='institution',
            name='titres',
            field=models.ManyToManyField(blank=True, to='mandats.Titre'),
        ),
    ]
