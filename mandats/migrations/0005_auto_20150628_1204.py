# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mandats', '0004_auto_20150425_2236'),
    ]

    operations = [
        migrations.CreateModel(
            name='Titre',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nom', models.CharField(max_length=1023)),
            ],
            options={
                'permissions': (('gere_les_mandats', 'gère les mandats'),),
            },
        ),
        migrations.AlterField(
            model_name='detenteur',
            name='titre',
            field=models.ForeignKey(to='mandats.Titre'),
        ),
    ]
