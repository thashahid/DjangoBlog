# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-15 16:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_blogpost_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='month_published',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='year_published',
            field=models.IntegerField(null=True),
        ),
    ]
