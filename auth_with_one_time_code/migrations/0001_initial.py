# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('fichiers_adherents', '0007_auto_20150629_2155'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Credentials',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('code', models.CharField(max_length=6, default='YWGYJC')),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('code', models.CharField(max_length=32, default='690V54E5EPVT8E4GZKDU5GC4BVVJL1M2')),
                ('date', models.DateTimeField(auto_now=True)),
                ('adherent', models.ForeignKey(to='fichiers_adherents.Adhérent')),
            ],
        ),
    ]
