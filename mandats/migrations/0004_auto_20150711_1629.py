# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mandats', '0003_institution_titres'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='institution',
            name='titres',
        ),
        migrations.AlterField(
            model_name='institution',
            name='meta_institution',
            field=models.ForeignKey(help_text="De quel type d'institution s'agit-il ?", to='mandats.MetaInstitution', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='institution',
            name='prefixe',
            field=models.CharField(max_length=10, help_text="Permet d'associer verbalement un titre à une institution, par exemple Président *du* Mouvement Démocrate, ou Maire *de* Viroflay."),
        ),
        migrations.AlterField(
            model_name='metainstitution',
            name='titres_par_defaut',
            field=models.ManyToManyField(help_text="Les titres généralement associés à ce type d'institution", blank=True, to='mandats.Titre'),
        ),
    ]
