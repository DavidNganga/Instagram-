# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-10 08:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0005_profile_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='images',
            new_name='user',
        ),
    ]
