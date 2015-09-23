# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membres', '0004_auto_20150916_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='nom_courant',
            field=models.CharField(default='Anonyme', max_length=255),
        ),
    ]
