# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-02-12 11:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopcart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopcart',
            name='shop_id',
            field=models.ForeignKey(db_column='shop_id', on_delete=django.db.models.deletion.CASCADE, to='shop.JdShop'),
        ),
        migrations.AlterField(
            model_name='shopcart',
            name='uid',
            field=models.ForeignKey(db_column='uid', on_delete=django.db.models.deletion.CASCADE, to='account.User'),
        ),
    ]
