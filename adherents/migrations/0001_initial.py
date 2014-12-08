# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('fichiers_adherents', '__first__'),
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('user', models.OneToOneField(serialize=False, to=settings.AUTH_USER_MODEL, primary_key=True)),
                ('nom_courant', models.CharField(max_length=255, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('adherent', models.OneToOneField(to='fichiers_adherents.Adhérent', blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
