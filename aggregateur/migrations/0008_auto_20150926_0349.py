# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('aggregateur', '0007_auto_20150925_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='description',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='channel',
            name='name',
            field=models.CharField(max_length=32, verbose_name='nom', unique=True),
        ),
        migrations.AlterField(
            model_name='channel',
            name='slug',
            field=autoslug.fields.AutoSlugField(max_length=64, unique=True),
        ),
    ]
