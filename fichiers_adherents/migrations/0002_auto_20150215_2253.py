# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fichiers_adherents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adhérent',
            name='importé_par_le_fichier',
            field=models.ForeignKey(blank=True, to='fichiers_adherents.FichierAdhérents'),
        ),
    ]
