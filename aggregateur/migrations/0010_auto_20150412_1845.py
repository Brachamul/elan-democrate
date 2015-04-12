# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aggregateur', '0009_auto_20150411_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(null=True, max_length=10000, blank=True),
        ),
    ]
