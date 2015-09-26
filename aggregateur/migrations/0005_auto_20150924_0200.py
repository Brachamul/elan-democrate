# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aggregateur', '0004_auto_20150924_0149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='description',
            field=models.CharField(default="Cette chaîne n'a pas encore de description.", max_length=255),
        ),
    ]
