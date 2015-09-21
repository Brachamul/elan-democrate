# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membres', '0005_auto_20150916_2338'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='twitter',
            field=models.CharField(null=True, help_text='Sans le @', max_length=255, blank=True),
        ),
    ]
