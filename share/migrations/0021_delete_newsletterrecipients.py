# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-22 20:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0020_auto_20180517_1124'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NewsLetterRecipients',
        ),
    ]