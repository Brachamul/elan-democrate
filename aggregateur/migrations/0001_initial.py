# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import autoslug.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('official', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(max_length=10000)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_edit', models.DateTimeField(default=None)),
                ('deleted', models.BooleanField(default=False)),
                ('health', models.IntegerField(default=0)),
                ('rank', models.IntegerField(default=0)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('parent_comment', models.ForeignKey(to='aggregateur.Comment', blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CommentVote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('color', models.CharField(choices=[('POS', 'positif'), ('NEG', 'négatif'), ('NEU', 'neutre')], max_length=24)),
                ('comment', models.ForeignKey(to='aggregateur.Comment')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LastRanking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('format', models.CharField(choices=[('LINK', 'link'), ('TEXT', 'text')], max_length=255)),
                ('title', models.CharField(max_length=144)),
                ('slug', autoslug.fields.AutoSlugField(populate_from='title', unique_with=('date',), editable=False)),
                ('content', models.TextField(null=True, blank=True, max_length=10000)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_edit', models.DateTimeField(default=None)),
                ('deleted', models.BooleanField(default=False)),
                ('health', models.IntegerField(default=0)),
                ('rank', models.IntegerField(default=0)),
                ('illustration', models.URLField(null=True, blank=True, max_length=2000)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('channel', models.ForeignKey(to='aggregateur.Channel', blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('color', models.CharField(choices=[('POS', 'positif'), ('NEG', 'négatif'), ('NEU', 'neutre')], max_length=24)),
                ('post', models.ForeignKey(to='aggregateur.Post')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='parent_post',
            field=models.ForeignKey(to='aggregateur.Post', blank=True, null=True),
        ),
    ]
