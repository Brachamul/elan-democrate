# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mandats', '0006_detenteur_peut_voir_la_federation'),
    ]

    operations = [
        migrations.AddField(
            model_name='mandat',
            name='code',
            field=models.CharField(help_text="Dans le cas d'une fédéation JDem, c'est le numéro de fédé, par exemple '78'.", blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='detenteur',
            name='date_de_debut',
            field=models.DateField(help_text="En cas d'arrivée après le début du mandat", blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='detenteur',
            name='date_de_fin',
            field=models.DateField(help_text='En cas de départ avant la fin du mandat', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='detenteur',
            name='peut_voir_la_federation',
            field=models.ManyToManyField(to='datascope.VueFederation', blank=True),
        ),
    ]
