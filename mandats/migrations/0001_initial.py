# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detenteur',
            fields=[
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, serialize=False, primary_key=True)),
                ('titre', models.CharField(max_length=1023)),
                ('charge', models.CharField(max_length=1023, blank=True, null=True)),
                ('date_de_debut', models.DateField(blank=True, null=True)),
                ('date_de_fin', models.DateField(blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=1023)),
                ('prefixe', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mandat',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('date_de_debut', models.DateField(blank=True, null=True)),
                ('date_de_fin', models.DateField(blank=True, null=True)),
                ('institution', models.ForeignKey(to='mandats.Institution')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MetaInstitution',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='institution',
            name='classe',
            field=models.ForeignKey(blank=True, to='mandats.MetaInstitution', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detenteur',
            name='mandat',
            field=models.OneToOneField(to='mandats.Mandat'),
            preserve_default=True,
        ),
    ]
