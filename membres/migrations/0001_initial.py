# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import membres.models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fichiers_adherents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_courant', models.CharField(max_length=255, default=membres.models.Profil.nomizateur)),
                ('bio', models.TextField(blank=True, max_length=255, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('adherent', models.OneToOneField(blank=True, to='fichiers_adherents.Adherent', on_delete=django.db.models.deletion.SET_NULL, null=True)),
                ('user', models.OneToOneField(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
