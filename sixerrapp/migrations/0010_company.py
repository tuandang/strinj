# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2019-01-02 10:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sixerrapp', '0009_remove_gig_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('url', models.TextField()),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('gig', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sixerrapp.Gig')),
            ],
        ),
    ]
