# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('post_type', models.CharField(choices=[('LINK', 'link'), ('TEXT', 'text')], max_length=255)),
                ('title', models.CharField(max_length=144)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, max_length=255)),
                ('content', models.TextField(max_length=10000)),
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
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('official', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='aggregateur.Tag'),
            preserve_default=True,
        ),
    ]
