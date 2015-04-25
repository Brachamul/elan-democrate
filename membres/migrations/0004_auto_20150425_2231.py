# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membres', '0003_auto_20150425_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID'),
        ),
    ]
