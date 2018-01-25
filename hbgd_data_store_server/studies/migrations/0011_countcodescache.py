# Copyright 2017-present, Bill & Melinda Gates Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-29 22:46
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studies', '0010_auto_20170127_0118'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountCodesCache',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cache', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, editable=False, null=True, size=None)),
                ('count', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='codes_cache', to='studies.Count')),
            ],
        ),
    ]
