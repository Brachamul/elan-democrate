# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Adherent',
            fields=[
                ('num_adhérent', models.IntegerField(serialize=False, primary_key=True)),
                ('fédération', models.IntegerField(null=True, blank=True)),
                ('date_première_adhésion', models.DateField(null=True, blank=True)),
                ('date_dernière_cotisation', models.DateField(null=True, blank=True)),
                ('nom', models.CharField(null=True, max_length=255, blank=True)),
                ('prénom', models.CharField(null=True, max_length=255, blank=True)),
                ('code_postal', models.IntegerField(null=True, blank=True)),
                ('ville', models.CharField(null=True, max_length=255, blank=True)),
                ('pays', models.CharField(null=True, max_length=255, blank=True)),
                ('date_de_naissance', models.DateField(null=True, blank=True)),
                ('profession', models.CharField(null=True, max_length=255, blank=True)),
                ('tel_portable', models.CharField(null=True, max_length=255, blank=True)),
                ('tel_bureau', models.CharField(null=True, max_length=255, blank=True)),
                ('tel_domicile', models.CharField(null=True, max_length=255, blank=True)),
                ('email', models.CharField(null=True, max_length=255, blank=True)),
                ('mandats', models.CharField(null=True, max_length=255, blank=True)),
                ('commune', models.CharField(null=True, max_length=255, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='AdherentDuFichier',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('fédération', models.IntegerField(null=True)),
                ('date_première_adhésion', models.DateField(null=True)),
                ('date_dernière_cotisation', models.DateField(null=True)),
                ('num_adhérent', models.IntegerField(null=True)),
                ('nom', models.CharField(null=True, max_length=255)),
                ('prénom', models.CharField(null=True, max_length=255)),
                ('code_postal', models.IntegerField(null=True)),
                ('ville', models.CharField(null=True, max_length=255)),
                ('pays', models.CharField(null=True, max_length=255)),
                ('date_de_naissance', models.DateField(null=True)),
                ('profession', models.CharField(null=True, max_length=255)),
                ('tel_portable', models.CharField(null=True, max_length=255)),
                ('tel_bureau', models.CharField(null=True, max_length=255)),
                ('tel_domicile', models.CharField(null=True, max_length=255)),
                ('email', models.CharField(null=True, max_length=255)),
                ('mandats', models.CharField(null=True, max_length=255)),
                ('commune', models.CharField(null=True, max_length=255)),
                ('adhérent', models.ForeignKey(null=True, to='fichiers_adherents.Adherent')),
            ],
            options={
                'verbose_name_plural': b'adh\xc3\xa9rents du fichier',
            },
        ),
        migrations.CreateModel(
            name='FichierAdherents',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('date_d_import', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(max_length=255)),
                ('fichier_csv', models.FileField(upload_to='fichiers_adherents/')),
                ('nombre_nouveaux_adherents', models.PositiveSmallIntegerField(null=True, blank=True, default=0)),
                ('nombre_readhesions', models.PositiveSmallIntegerField(null=True, blank=True, default=0)),
                ('importateur', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': b'fichiers adh\xc3\xa9rents',
                'permissions': (('peut_televerser', 'peut téléverser'),),
            },
        ),
        migrations.AddField(
            model_name='adherentdufichier',
            name='fichier',
            field=models.ForeignKey(to='fichiers_adherents.FichierAdherents'),
        ),
        migrations.AddField(
            model_name='adherent',
            name='importé_par_le_fichier',
            field=models.ForeignKey(to='fichiers_adherents.FichierAdherents', on_delete=django.db.models.deletion.SET_NULL, null=True, blank=True),
        ),
    ]
