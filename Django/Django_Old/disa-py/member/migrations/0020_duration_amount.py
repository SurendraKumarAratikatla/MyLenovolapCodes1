# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-05 03:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0019_auto_20160704_0211'),
    ]

    operations = [
        migrations.AddField(
            model_name='duration',
            name='amount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
