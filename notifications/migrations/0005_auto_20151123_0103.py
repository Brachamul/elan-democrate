# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0004_auto_20151121_0224'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Notification',
        ),
        migrations.AlterField(
            model_name='notificationevent',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True),
        ),
    ]
