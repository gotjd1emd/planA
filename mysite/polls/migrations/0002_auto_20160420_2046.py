# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-20 11:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Posts',
            new_name='Post',
        ),
    ]
