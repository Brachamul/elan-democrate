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
                ('genre', models.CharField(blank=True, max_length=255)),
                ('nom', models.CharField(max_length=255)),
                ('prénom', models.CharField(max_length=255)),
                ('adresse_1', models.CharField(blank=True, max_length=255)),
                ('adresse_2', models.CharField(blank=True, max_length=255)),
                ('adresse_3', models.CharField(blank=True, max_length=255)),
                ('adresse_4', models.CharField(blank=True, max_length=255)),
                ('code_postal', models.IntegerField(blank=True)),
                ('ville', models.CharField(blank=True, max_length=255)),
                ('pays', models.CharField(blank=True, max_length=255)),
                ('date_de_naissance', models.DateField()),
                ('profession', models.CharField(blank=True, max_length=255)),
                ('tel_portable', models.CharField(blank=True, max_length=255)),
                ('tel_bureau', models.CharField(blank=True, max_length=255)),
                ('tel_domicile', models.CharField(blank=True, max_length=255)),
                ('email', models.CharField(blank=True, max_length=255)),
                ('mandats', models.CharField(blank=True, max_length=255)),
                ('commune', models.CharField(blank=True, max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AdhérentDuFichier',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
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
                ('adhérent', models.ForeignKey(to='fichiers_adhérents.Adhérent', null=True)),
            ],
            options={
                'verbose_name_plural': 'adhérents du fichier',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FichierAdhérents',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('importé_à_date', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(max_length=255)),
                ('fichier_csv', models.FileField(upload_to='fichiers_adherents/')),
                ('nombre_nouveaux_adhérents', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('nombre_réadhésions', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('nombre_autres_mises_à_jour', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('importateur', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'fichiers adhérents',
                'permissions': (('peut_televerser', 'peut téléverser'),),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='adhérentdufichier',
            name='fichier',
            field=models.ForeignKey(to='fichiers_adhérents.FichierAdhérents'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='adhérent',
            name='importé_par_le_fichier',
            field=models.ForeignKey(to='fichiers_adhérents.FichierAdhérents'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='adhérent',
            name='user',
            field=models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
