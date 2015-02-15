# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fichiers_adherents', '0002_auto_20150215_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adhérent',
            name='importé_par_le_fichier',
            field=models.ForeignKey(null=True, to='fichiers_adherents.FichierAdhérents', blank=True),
        ),
    ]
