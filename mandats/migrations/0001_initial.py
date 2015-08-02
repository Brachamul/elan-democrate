# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membres', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detenteur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charge', models.CharField(blank=True, max_length=1023, null=True)),
                ('date_de_debut', models.DateField(blank=True, help_text="En cas d'arrivée après le début du mandat", null=True)),
                ('date_de_fin', models.DateField(blank=True, help_text='En cas de départ avant la fin du mandat', null=True)),
            ],
            options={
                'permissions': (('gere_les_mandats', 'gère les mandats'),),
            },
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=1023)),
                ('prefixe', models.CharField(help_text="Permet d'associer verbalement un titre à une institution, par exemple Président *du* Mouvement Démocrate, ou Maire *de* Viroflay.", max_length=10)),
            ],
            options={
                'permissions': (('gere_les_mandats', 'gère les mandats'),),
            },
        ),
        migrations.CreateModel(
            name='Mandat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_de_debut', models.DateField(null=True)),
                ('date_de_fin', models.DateField(blank=True, null=True)),
                ('institution', models.ForeignKey(to='mandats.Institution')),
            ],
            options={
                'permissions': (('gere_les_mandats', 'gère les mandats'),),
            },
        ),
        migrations.CreateModel(
            name='MetaInstitution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
            ],
            options={
                'permissions': (('gere_les_mandats', 'gère les mandats'),),
            },
        ),
        migrations.CreateModel(
            name='Titre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'permissions': (('gere_les_mandats', 'gère les mandats'),),
            },
        ),
        migrations.AddField(
            model_name='metainstitution',
            name='titres_par_defaut',
            field=models.ManyToManyField(blank=True, help_text="Les titres généralement associés à ce type d'institution", to='mandats.Titre'),
        ),
        migrations.AddField(
            model_name='institution',
            name='meta_institution',
            field=models.ForeignKey(blank=True, help_text="De quel type d'institution s'agit-il ?", to='mandats.MetaInstitution', null=True),
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
