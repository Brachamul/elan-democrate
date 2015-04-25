# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membres', '0005_profil_user'),
        ('mandats', '0003_auto_20150425_0113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detenteur',
            name='user',
        ),
        migrations.AddField(
            model_name='detenteur',
            name='profil',
            field=models.ForeignKey(to='membres.Profil', default=1),
            preserve_default=False,
        ),
    ]
