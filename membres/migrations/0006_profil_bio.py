# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membres', '0005_profil_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='bio',
            field=models.TextField(max_length=255, null=True, blank=True),
        ),
    ]
