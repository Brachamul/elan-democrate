# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aggregateur', '0006_auto_20150327_1241'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('content', models.TextField(max_length=10000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('parent_comment', models.ForeignKey(null=True, to='aggregateur.Comment', blank=True)),
                ('parent_post', models.ForeignKey(null=True, to='aggregateur.Post', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
