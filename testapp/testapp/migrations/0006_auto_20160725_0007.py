# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-24 15:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0005_auto_20160725_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adjustment',
            name='adjustment_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 25, 0, 7, 45, 332365), verbose_name=b'date adjusted'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_adjustment_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 25, 0, 7, 45, 333192), verbose_name=b'date adjusted'),
        ),
    ]
