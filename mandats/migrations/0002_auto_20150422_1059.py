# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('mandats', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='detenteur',
            options={'permissions': (('gere_les_mandats', 'gère les mandats'),)},
        ),
        migrations.AlterModelOptions(
            name='institution',
            options={'permissions': (('gere_les_mandats', 'gère les mandats'),)},
        ),
        migrations.AlterModelOptions(
            name='mandat',
            options={'permissions': (('gere_les_mandats', 'gère les mandats'),)},
        ),
        migrations.AlterModelOptions(
            name='metainstitution',
            options={'permissions': (('gere_les_mandats', 'gère les mandats'),)},
        ),
        migrations.AlterField(
            model_name='detenteur',
            name='mandat',
            field=models.ForeignKey(to='mandats.Mandat'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='detenteur',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, primary_key=True, serialize=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mandat',
            name='date_de_debut',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
    ]
