# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adherents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='nom_courant',
            field=models.CharField(null=True, max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='profil',
            name='notes',
            field=models.TextField(null=True, blank=True),
        ),
    ]
