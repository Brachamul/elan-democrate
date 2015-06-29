# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fichiers_adherents', '0006_auto_20150613_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adhérent',
            name='importé_par_le_fichier',
            field=models.ForeignKey(null=True, to='fichiers_adherents.FichierAdhérents', blank=True, on_delete=django.db.models.deletion.SET_NULL),
        ),
    ]
