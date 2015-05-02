# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membres', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='user',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
