# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fichiers_adhérents', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fichieradhérents',
            name='nombre_autres_mises_à_jour',
        ),
        migrations.RemoveField(
            model_name='fichieradhérents',
            name='nombre_nouveaux_adhérents',
        ),
    ]
