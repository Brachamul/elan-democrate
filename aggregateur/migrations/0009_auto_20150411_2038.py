# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('aggregateur', '0008_lastranking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=django_markdown.models.MarkdownField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=django_markdown.models.MarkdownField(max_length=10000, blank=True, null=True),
        ),
    ]
