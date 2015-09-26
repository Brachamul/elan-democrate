# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beta', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='betacandidat',
            name='telephone',
        ),
        migrations.AddField(
            model_name='betacandidat',
            name='compte_twitter',
            field=models.CharField(null=True, max_length=32, blank=True, help_text='Sans le @!'),
        ),
    ]
