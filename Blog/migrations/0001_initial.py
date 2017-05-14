# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-14 17:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=200)),
                ('post_body', models.TextField()),
                ('date_published', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
