# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-07 12:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0004_usersperchannel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usersperchannel',
            old_name='Socail',
            new_name='Social',
        ),
    ]
