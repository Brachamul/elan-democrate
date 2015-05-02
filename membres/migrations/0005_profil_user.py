# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('membres', '0004_auto_20150425_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='user',
            field=models.OneToOneField(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
