'''
    Copyright (C) 2017 Gitcoin Core 

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

'''
# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-16 23:30
from __future__ import unicode_literals

import datetime
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bounty',
            name='bounty_owner_address',
            field=models.CharField(default='0x0', max_length=30),
        ),
        migrations.AddField(
            model_name='bounty',
            name='claimeee_address',
            field=models.CharField(default='0x0', max_length=30),
        ),
        migrations.AddField(
            model_name='bounty',
            name='expires_date',
            field=models.DateField(default=datetime.datetime(2017, 9, 16, 23, 30, 30, 669947, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='bounty',
            name='github_url',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='bounty',
            name='is_open',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='bounty',
            name='raw_data',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}),
        ),
    ]
