# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BetaCandidat',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('nom_courant', models.CharField(max_length=255, verbose_name='Prénom et Nom')),
                ('email', models.EmailField(help_text='Idéalement celle que le MoDem a dans son fichier', max_length=254)),
                ('fonctions', models.CharField(help_text="Si vous êtes quelqu'un d'important", null=True, blank=True, max_length=1024)),
                ('telephone', models.CharField(max_length=20, null=True, blank=True)),
            ],
        ),
    ]
