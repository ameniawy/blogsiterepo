# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-27 11:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='username',
            field=models.CharField(default='anon', max_length=100),
            preserve_default=False,
        ),
    ]
