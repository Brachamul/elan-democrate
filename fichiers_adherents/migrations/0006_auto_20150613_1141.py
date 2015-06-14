# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fichiers_adherents', '0005_auto_20150505_2214'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fichieradhérents',
            old_name='importé_à_date',
            new_name='date_d_import',
        ),
    ]
