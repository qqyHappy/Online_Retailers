# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-01-24 12:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JdBrand',
            fields=[
                ('brand_id', models.AutoField(primary_key=True, serialize=False)),
                ('brand_name', models.CharField(max_length=64)),
                ('third_cate_id', models.ForeignKey(db_column='third_cate_id', on_delete=django.db.models.deletion.CASCADE, to='main.JdThirdCate')),
            ],
        ),
    ]
