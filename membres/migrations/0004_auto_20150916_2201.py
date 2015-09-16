# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membres', '0003_auto_20150916_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='nom_courant',
            field=models.CharField(max_length=255),
        ),
    ]
