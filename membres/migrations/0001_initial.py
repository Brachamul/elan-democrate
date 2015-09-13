# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import membres.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('fichiers_adherents', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nom_courant', models.CharField(max_length=255, default=membres.models.Profil.nomizateur)),
                ('bio', models.TextField(null=True, max_length=255, blank=True)),
                ('notes', models.TextField(null=True, blank=True)),
                ('adherent', models.OneToOneField(to='fichiers_adherents.Adherent', on_delete=django.db.models.deletion.SET_NULL, null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, null=True, blank=True)),
            ],
        ),
    ]
