# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fichiers_adherents', '0003_auto_20150215_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adhérent',
            name='adresse_1',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='adhérent',
            name='adresse_2',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='adhérent',
            name='adresse_3',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='adhérent',
            name='adresse_4',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='adhérent',
            name='code_postal',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='adhérent',
            name='commune',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='adhérent',
            name='date_de_naissance',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='adhérent',
            name='date_dernière_cotisation',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='adhérent',
            name='date_première_adhésion',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='adhérent',
            name='email',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='adhérent',
            name='fédération',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='adhérent',
            name='genre',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='adhérent',
            name='mandats',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='adhérent',
            name='nom',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='adhérent',
            name='pays',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='adhérent',
            name='profession',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='adhérent',
            name='prénom',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='adhérent',
            name='tel_bureau',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='adhérent',
            name='tel_domicile',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='adhérent',
            name='tel_portable',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='adhérent',
            name='ville',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
    ]
