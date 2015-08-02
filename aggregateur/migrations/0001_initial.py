# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('official', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=10000)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_edit', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('health', models.IntegerField(default=0)),
                ('rank', models.IntegerField(default=0)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('parent_comment', models.ForeignKey(blank=True, to='aggregateur.Comment', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CommentVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(choices=[('POS', 'positif'), ('NEG', 'négatif'), ('NEU', 'neutre')], max_length=24)),
                ('comment', models.ForeignKey(to='aggregateur.Comment')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LastRanking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('format', models.CharField(choices=[('LINK', 'link'), ('TEXT', 'text')], max_length=255)),
                ('title', models.CharField(max_length=144)),
                ('slug', autoslug.fields.AutoSlugField(max_length=255, editable=False)),
                ('content', models.TextField(blank=True, max_length=10000, null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('health', models.IntegerField(default=0)),
                ('rank', models.IntegerField(default=0)),
                ('illustration', models.URLField(blank=True, max_length=2000, null=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('channel', models.ForeignKey(blank=True, to='aggregateur.Channel', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(choices=[('POS', 'positif'), ('NEG', 'négatif'), ('NEU', 'neutre')], max_length=24)),
                ('post', models.ForeignKey(to='aggregateur.Post')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='parent_post',
            field=models.ForeignKey(blank=True, to='aggregateur.Post', null=True),
        ),
    ]
