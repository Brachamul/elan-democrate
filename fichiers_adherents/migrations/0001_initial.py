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
                ('nom', models.CharField(max_length=255, null=True, blank=True)),
                ('prénom', models.CharField(max_length=255, null=True, blank=True)),
                ('code_postal', models.IntegerField(null=True, blank=True)),
                ('ville', models.CharField(max_length=255, null=True, blank=True)),
                ('pays', models.CharField(max_length=255, null=True, blank=True)),
                ('date_de_naissance', models.DateField(null=True, blank=True)),
                ('profession', models.CharField(max_length=255, null=True, blank=True)),
                ('tel_portable', models.CharField(max_length=255, null=True, blank=True)),
                ('tel_bureau', models.CharField(max_length=255, null=True, blank=True)),
                ('tel_domicile', models.CharField(max_length=255, null=True, blank=True)),
                ('email', models.CharField(max_length=255, null=True, blank=True)),
                ('mandats', models.CharField(max_length=255, null=True, blank=True)),
                ('commune', models.CharField(max_length=255, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='AdherentDuFichier',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('fédération', models.IntegerField(null=True)),
                ('date_première_adhésion', models.DateField(null=True)),
                ('date_dernière_cotisation', models.DateField(null=True)),
                ('num_adhérent', models.IntegerField(null=True)),
                ('nom', models.CharField(max_length=255, null=True)),
                ('prénom', models.CharField(max_length=255, null=True)),
                ('code_postal', models.IntegerField(null=True)),
                ('ville', models.CharField(max_length=255, null=True)),
                ('pays', models.CharField(max_length=255, null=True)),
                ('date_de_naissance', models.DateField(null=True)),
                ('profession', models.CharField(max_length=255, null=True)),
                ('tel_portable', models.CharField(max_length=255, null=True)),
                ('tel_bureau', models.CharField(max_length=255, null=True)),
                ('tel_domicile', models.CharField(max_length=255, null=True)),
                ('email', models.CharField(max_length=255, null=True)),
                ('mandats', models.CharField(max_length=255, null=True)),
                ('commune', models.CharField(max_length=255, null=True)),
                ('adhérent', models.ForeignKey(to='fichiers_adherents.Adherent', null=True)),
            ],
            options={
                'verbose_name_plural': b'adh\xc3\xa9rents du fichier',
            },
        ),
        migrations.CreateModel(
            name='FichierAdherents',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('date_d_import', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(max_length=255)),
                ('fichier_csv', models.FileField(upload_to='fichiers_adherents/')),
                ('nombre_nouveaux_adherents', models.PositiveSmallIntegerField(default=0, null=True, blank=True)),
                ('nombre_readhesions', models.PositiveSmallIntegerField(default=0, null=True, blank=True)),
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
