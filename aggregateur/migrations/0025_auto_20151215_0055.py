# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-15 00:55
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aggregateur', '0024_auto_20151118_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=True, max_length=64, populate_from='name', unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, max_length=255, populate_from='title', unique_with=('date__year',)),
        ),
    ]
