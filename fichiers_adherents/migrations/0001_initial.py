# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Adherent',
            fields=[
                ('num_adhérent', models.IntegerField(primary_key=True, serialize=False)),
                ('fédération', models.IntegerField(blank=True, null=True)),
                ('date_première_adhésion', models.DateField(blank=True, null=True)),
                ('date_dernière_cotisation', models.DateField(blank=True, null=True)),
                ('nom', models.CharField(blank=True, max_length=255, null=True)),
                ('prénom', models.CharField(blank=True, max_length=255, null=True)),
                ('code_postal', models.IntegerField(blank=True, null=True)),
                ('ville', models.CharField(blank=True, max_length=255, null=True)),
                ('pays', models.CharField(blank=True, max_length=255, null=True)),
                ('date_de_naissance', models.DateField(blank=True, null=True)),
                ('profession', models.CharField(blank=True, max_length=255, null=True)),
                ('tel_portable', models.CharField(blank=True, max_length=255, null=True)),
                ('tel_bureau', models.CharField(blank=True, max_length=255, null=True)),
                ('tel_domicile', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('mandats', models.CharField(blank=True, max_length=255, null=True)),
                ('commune', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AdherentDuFichier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('adhérent', models.ForeignKey(null=True, to='fichiers_adherents.Adherent')),
            ],
            options={
                'verbose_name_plural': 'adhérents du fichier',
            },
        ),
        migrations.CreateModel(
            name='FichierAdherents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_d_import', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(max_length=255)),
                ('fichier_csv', models.FileField(upload_to='fichiers_adherents/')),
                ('nombre_nouveaux_adherents', models.PositiveSmallIntegerField(blank=True, null=True, default=0)),
                ('nombre_réadhésions', models.PositiveSmallIntegerField(blank=True, null=True, default=0)),
                ('importateur', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'fichiers adhérents',
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
            field=models.ForeignKey(blank=True, to='fichiers_adherents.FichierAdherents', on_delete=django.db.models.deletion.SET_NULL, null=True),
        ),
    ]
