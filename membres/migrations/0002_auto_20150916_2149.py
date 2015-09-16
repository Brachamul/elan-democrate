# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import membres.models


class Migration(migrations.Migration):

    dependencies = [
        ('membres', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='nom_courant',
            field=models.CharField(max_length=255, default="Anonyme"),
        ),
    ]
