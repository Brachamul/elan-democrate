# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membres', '0007_auto_20150629_2155'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detenteur',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('charge', models.CharField(max_length=1023, null=True, blank=True)),
                ('date_de_debut', models.DateField(help_text="En cas d'arrivée après le début du mandat", blank=True, null=True)),
                ('date_de_fin', models.DateField(help_text='En cas de départ avant la fin du mandat', blank=True, null=True)),
            ],
            options={
                'permissions': (('gere_les_mandats', 'gère les mandats'),),
            },
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=1023)),
                ('prefixe', models.CharField(max_length=10)),
            ],
            options={
                'permissions': (('gere_les_mandats', 'gère les mandats'),),
            },
        ),
        migrations.CreateModel(
            name='Mandat',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('date_de_debut', models.DateField(null=True)),
                ('date_de_fin', models.DateField(null=True, blank=True)),
                ('institution', models.ForeignKey(to='mandats.Institution')),
            ],
            options={
                'permissions': (('gere_les_mandats', 'gère les mandats'),),
            },
        ),
        migrations.CreateModel(
            name='MetaInstitution',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=255)),
            ],
            options={
                'permissions': (('gere_les_mandats', 'gère les mandats'),),
            },
        ),
        migrations.CreateModel(
            name='Titre',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=1023)),
            ],
            options={
                'permissions': (('gere_les_mandats', 'gère les mandats'),),
            },
        ),
        migrations.AddField(
            model_name='metainstitution',
            name='titres_par_defaut',
            field=models.ManyToManyField(blank=True, to='mandats.Titre'),
        ),
        migrations.AddField(
            model_name='institution',
            name='meta_institution',
            field=models.ForeignKey(blank=True, to='mandats.MetaInstitution', null=True),
        ),
        migrations.AddField(
            model_name='detenteur',
            name='mandat',
            field=models.ForeignKey(to='mandats.Mandat'),
        ),
        migrations.AddField(
            model_name='detenteur',
            name='profil',
            field=models.ForeignKey(to='membres.Profil'),
        ),
        migrations.AddField(
            model_name='detenteur',
            name='titre',
            field=models.ForeignKey(to='mandats.Titre'),
        ),
    ]
