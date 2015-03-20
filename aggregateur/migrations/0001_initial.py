# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('official', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('post_type', models.CharField(max_length=255, choices=[('LINK', 'link'), ('TEXT', 'text')])),
                ('title', models.CharField(max_length=144)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, max_length=255)),
                ('content', models.TextField(blank=True, null=True, max_length=10000)),
                ('date', models.DateTimeField(auto_now=True)),
                ('score', models.IntegerField(default=0)),
                ('illustration', models.URLField(blank=True, null=True, max_length=2000)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('color', models.CharField(max_length=24, choices=[('POS', 'positif'), ('NEG', 'négatif'), ('NEU', 'neutre')])),
                ('post', models.ForeignKey(to='aggregateur.Post')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
