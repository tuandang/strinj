# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2019-06-13 06:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sixerrapp', '0007_auto_20190227_1949'),
    ]

    operations = [
#         migrations.AddField(
#             model_name='profile',
#             name='company',
#             field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sixerrapp.Company'),
#         ),
        migrations.AlterField(
            model_name='profile',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='resumes'),
        ),
    ]
