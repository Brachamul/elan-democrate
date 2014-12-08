# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Adhérent',
            fields=[
                ('num_adhérent', models.IntegerField(serialize=False, primary_key=True)),
                ('fédération', models.IntegerField()),
                ('date_première_adhésion', models.DateField()),
                ('date_dernière_cotisation', models.DateField()),
                ('genre', models.CharField(max_length=255, blank=True)),
                ('nom', models.CharField(max_length=255)),
                ('prénom', models.CharField(max_length=255)),
                ('adresse_1', models.CharField(max_length=255, blank=True)),
                ('adresse_2', models.CharField(max_length=255, blank=True)),
                ('adresse_3', models.CharField(max_length=255, blank=True)),
                ('adresse_4', models.CharField(max_length=255, blank=True)),
                ('code_postal', models.IntegerField(blank=True)),
                ('ville', models.CharField(max_length=255, blank=True)),
                ('pays', models.CharField(max_length=255, blank=True)),
                ('date_de_naissance', models.DateField()),
                ('profession', models.CharField(max_length=255, blank=True)),
                ('tel_portable', models.CharField(max_length=255, blank=True)),
                ('tel_bureau', models.CharField(max_length=255, blank=True)),
                ('tel_domicile', models.CharField(max_length=255, blank=True)),
                ('email', models.CharField(max_length=255, blank=True)),
                ('mandats', models.CharField(max_length=255, blank=True)),
                ('commune', models.CharField(max_length=255, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AdhérentDuFichier',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('fédération', models.IntegerField()),
                ('date_première_adhésion', models.DateField()),
                ('date_dernière_cotisation', models.DateField()),
                ('num_adhérent', models.IntegerField()),
                ('genre', models.CharField(max_length=255)),
                ('nom', models.CharField(max_length=255)),
                ('prénom', models.CharField(max_length=255)),
                ('adresse_1', models.CharField(max_length=255)),
                ('adresse_2', models.CharField(max_length=255)),
                ('adresse_3', models.CharField(max_length=255)),
                ('adresse_4', models.CharField(max_length=255)),
                ('code_postal', models.IntegerField()),
                ('ville', models.CharField(max_length=255)),
                ('pays', models.CharField(max_length=255)),
                ('npai', models.BooleanField(default=False)),
                ('date_de_naissance', models.DateField()),
                ('profession', models.CharField(max_length=255)),
                ('tel_portable', models.CharField(max_length=255)),
                ('tel_bureau', models.CharField(max_length=255)),
                ('tel_domicile', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('mandats', models.CharField(max_length=255)),
                ('commune', models.CharField(max_length=255)),
                ('adhérent', models.ForeignKey(null=True, to='fichiers_adherents.Adhérent')),
            ],
            options={
                'verbose_name_plural': 'adhérents du fichier',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FichierAdhérents',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('importé_à_date', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(max_length=255)),
                ('fichier_csv', models.FileField(upload_to='fichiers_adherents/')),
                ('nombre_nouveaux_adherents', models.PositiveSmallIntegerField(blank=True, null=True, default=0)),
                ('nombre_réadhésions', models.PositiveSmallIntegerField(blank=True, null=True, default=0)),
                ('importateur', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('peut_televerser', 'peut téléverser'),),
                'verbose_name_plural': 'fichiers adhérents',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='adhérentdufichier',
            name='fichier',
            field=models.ForeignKey(to='fichiers_adherents.FichierAdhérents'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='adhérent',
            name='importé_par_le_fichier',
            field=models.ForeignKey(to='fichiers_adherents.FichierAdhérents'),
            preserve_default=True,
        ),
    ]
