# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-25 03:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200423_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='slug_padrao'),
            preserve_default=False,
        ),
    ]
