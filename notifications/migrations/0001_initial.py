# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('non_lu', models.BooleanField(default=True)),
                ('prevenu_par_email', models.BooleanField(default=False)),
                ('id_acteur', models.CharField(blank=True, max_length=255, null=True)),
                ('action', models.CharField(max_length=255)),
                ('id_cible', models.CharField(blank=True, max_length=255, null=True)),
                ('id_lieu', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('destinataire', models.ForeignKey(related_name='destinataire_de_la_notif', to=settings.AUTH_USER_MODEL)),
                ('type_acteur', models.ForeignKey(blank=True, to='contenttypes.ContentType', related_name='acteur_de_la_notif', null=True)),
                ('type_cible', models.ForeignKey(blank=True, to='contenttypes.ContentType', related_name='cible_de_la_notif', null=True)),
                ('type_lieu', models.ForeignKey(blank=True, to='contenttypes.ContentType', related_name='lieu_de_la_notif', null=True)),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
    ]
