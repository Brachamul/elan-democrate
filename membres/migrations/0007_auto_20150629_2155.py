# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('membres', '0006_profil_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='adherent',
            field=models.OneToOneField(null=True, to='fichiers_adherents.Adhérent', blank=True, on_delete=django.db.models.deletion.SET_NULL),
        ),
    ]
