# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fichiers_adherents', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Credentials',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('code', models.CharField(default='JS619C', max_length=6)),
                ('date', models.DateTimeField(auto_now=True)),
                ('attempts', models.PositiveSmallIntegerField(default=0)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Credentials',
            },
        ),
        migrations.CreateModel(
            name='EmailConfirmationInstance',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('code', models.CharField(default='9O48F2852GECVFFBD4CZSJDOUL8KEQK0', max_length=32)),
                ('date', models.DateTimeField(auto_now=True)),
                ('adherent', models.ForeignKey(to='fichiers_adherents.Adherent')),
            ],
        ),
    ]
