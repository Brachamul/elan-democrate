# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mandats', '0007_auto_20150629_2027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mandat',
            name='code',
        ),
        migrations.AddField(
            model_name='institution',
            name='code',
            field=models.CharField(blank=True, null=True, help_text="Dans le cas d'une fédéation JDem, c'est le numéro de fédé, par exemple '78'.", max_length=255),
        ),
    ]
