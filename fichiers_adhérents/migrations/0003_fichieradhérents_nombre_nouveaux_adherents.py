# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fichiers_adhérents', '0002_auto_20141111_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='fichieradhérents',
            name='nombre_nouveaux_adherents',
            field=models.PositiveSmallIntegerField(null=True, default=0, blank=True),
            preserve_default=True,
        ),
    ]
