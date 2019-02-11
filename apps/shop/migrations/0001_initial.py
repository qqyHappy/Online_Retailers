# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-01-25 01:19
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
            name='JdShop',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=80)),
                ('original_price', models.IntegerField()),
                ('promote_price', models.IntegerField()),
                ('img_url', models.CharField(max_length=256)),
                ('month_sales', models.IntegerField()),
                ('total_sales', models.IntegerField()),
                ('total_evaluates', models.IntegerField()),
                ('third_cate_id', models.ForeignKey(db_column='third_cate_id', on_delete=django.db.models.deletion.CASCADE, to='main.JdThirdCate')),
            ],
            options={
                'db_table': 'jd_shop',
            },
        ),
    ]
