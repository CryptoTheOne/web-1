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
# Generated by Django 1.11 on 2017-09-16 23:33
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20170916_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bounty',
            name='bounty_owner_address',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='bounty',
            name='bounty_type',
            field=models.CharField(choices=[('bug', 'bug'), ('security', 'security'), ('feature', 'feature'), ('unknown', 'unknown')], max_length=50),
        ),
        migrations.AlterField(
            model_name='bounty',
            name='claimeee_address',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='bounty',
            name='experience_level',
            field=models.CharField(choices=[('beginner', 'beginner'), ('intermediate', 'intermediate'), ('advanced', 'advanced'), ('unknown', 'unknown')], max_length=50),
        ),
        migrations.AlterField(
            model_name='bounty',
            name='expires_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='bounty',
            name='github_url',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='bounty',
            name='is_open',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='bounty',
            name='project_length',
            field=models.CharField(choices=[('hours', 'hours'), ('days', 'days'), ('weeks', 'weeks'), ('months', 'months'), ('unknown', 'unknown')], max_length=50),
        ),
        migrations.AlterField(
            model_name='bounty',
            name='raw_data',
            field=django.contrib.postgres.fields.jsonb.JSONField(),
        ),
        migrations.AlterField(
            model_name='bounty',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='bounty',
            name='token_address',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='bounty',
            name='token_name',
            field=models.CharField(max_length=50),
        ),
    ]
