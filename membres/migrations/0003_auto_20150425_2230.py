# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membres', '0002_auto_20150425_2229'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profil',
            old_name='user',
            new_name='id',
        ),
    ]
