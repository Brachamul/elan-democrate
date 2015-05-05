# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fichiers_adherents', '0004_auto_20150215_2256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adhérent',
            name='adresse_1',
        ),
        migrations.RemoveField(
            model_name='adhérent',
            name='adresse_2',
        ),
        migrations.RemoveField(
            model_name='adhérent',
            name='adresse_3',
        ),
        migrations.RemoveField(
            model_name='adhérent',
            name='adresse_4',
        ),
        migrations.RemoveField(
            model_name='adhérent',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='adhérentdufichier',
            name='adresse_1',
        ),
        migrations.RemoveField(
            model_name='adhérentdufichier',
            name='adresse_2',
        ),
        migrations.RemoveField(
            model_name='adhérentdufichier',
            name='adresse_3',
        ),
        migrations.RemoveField(
            model_name='adhérentdufichier',
            name='adresse_4',
        ),
        migrations.RemoveField(
            model_name='adhérentdufichier',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='adhérentdufichier',
            name='npai',
        ),
        migrations.AlterField(
            model_name='adhérentdufichier',
            name='code_postal',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='adhérentdufichier',
            name='commune',
            field=models.CharField(null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='adhérentdufichier',
            name='date_de_naissance',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='adhérentdufichier',
            name='date_dernière_cotisation',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='adhérentdufichier',
            name='date_première_adhésion',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='adhérentdufichier',
            name='email',
            field=models.CharField(null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='adhérentdufichier',
            name='fédération',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='adhérentdufichier',
            name='mandats',
            field=models.CharField(null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='adhérentdufichier',
            name='nom',
            field=models.CharField(null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='adhérentdufichier',
            name='num_adhérent',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='adhérentdufichier',
            name='pays',
            field=models.CharField(null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='adhérentdufichier',
            name='profession',
            field=models.CharField(null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='adhérentdufichier',
            name='prénom',
            field=models.CharField(null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='adhérentdufichier',
            name='tel_bureau',
            field=models.CharField(null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='adhérentdufichier',
            name='tel_domicile',
            field=models.CharField(null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='adhérentdufichier',
            name='tel_portable',
            field=models.CharField(null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='adhérentdufichier',
            name='ville',
            field=models.CharField(null=True, max_length=255),
        ),
    ]
