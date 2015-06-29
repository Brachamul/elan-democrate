# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datascope', '__first__'),
        ('mandats', '0005_auto_20150628_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='detenteur',
            name='peut_voir_la_federation',
            field=models.ManyToManyField(to='datascope.VueFederation'),
        ),
    ]
