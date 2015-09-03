# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aggregateur', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='last_edit',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='last_edit',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
