# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2019-01-02 09:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sixerrapp', '0008_auto_20190102_0312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gig',
            name='price',
        ),
    ]