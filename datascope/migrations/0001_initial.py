# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mandats', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='VueFederation',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('numero_de_federation', models.CharField(max_length=255, help_text="C'est le numéro de la fédé, par exemple '78'.")),
                ('federation', models.ForeignKey(to='mandats.Institution')),
                ('titres', models.ManyToManyField(help_text="Ce sont les titres qui permettent d'accéder aux données, par exemple 'secrétaire' et 'président'.", to='mandats.Titre')),
            ],
            options={
                'permissions': (('gere_les_mandats', 'gère les mandats'),),
            },
        ),
    ]
