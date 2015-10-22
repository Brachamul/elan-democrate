# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aggregateur', '0019_auto_20151022_1926'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('main_settings', models.BooleanField(default=True, unique=True)),
                ('welcome_text', models.TextField(max_length=1024, default='Bienvenue sur Élan Démocrate.')),
            ],
        ),
        migrations.DeleteModel(
            name='WelcomeText',
        ),
    ]
