# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('historical_data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricehistory',
            name='market_cap',
            field=models.PositiveIntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pricehistory',
            name='price',
            field=models.DecimalField(max_digits=8, decimal_places=2),
            preserve_default=True,
        ),
    ]
