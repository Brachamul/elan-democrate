# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('fichiers_adherents', '0004_auto_20150215_2256'),
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('user', models.OneToOneField(serialize=False, primary_key=True, to=settings.AUTH_USER_MODEL)),
                ('nom_courant', models.CharField(null=True, max_length=255, blank=True)),
                ('notes', models.TextField(null=True, blank=True)),
                ('adherent', models.OneToOneField(blank=True, null=True, to='fichiers_adherents.Adhérent')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
