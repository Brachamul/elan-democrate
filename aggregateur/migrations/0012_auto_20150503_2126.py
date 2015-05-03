# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aggregateur', '0011_comment_deleted'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentVote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('color', models.CharField(choices=[('POS', 'positif'), ('NEG', 'négatif'), ('NEU', 'neutre')], max_length=24)),
                ('post', models.ForeignKey(to='aggregateur.Post')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='health',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='rank',
            field=models.IntegerField(default=0),
        ),
    ]
