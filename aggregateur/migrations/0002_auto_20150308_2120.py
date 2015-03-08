# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aggregateur', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('color', models.CharField(choices=[('POS', 'positif'), ('NEG', 'négatif'), ('NEU', 'neutre')], max_length=24)),
                ('post', models.ForeignKey(to='aggregateur.Post')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=10000, null=True, blank=True),
        ),
    ]
