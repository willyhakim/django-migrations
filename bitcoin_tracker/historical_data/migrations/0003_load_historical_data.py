# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models, migrations
from datetime import date

def load_data(apps, schema_editor):
	PriceHistory = apps.get_model('historical_data', 'PriceHistory')

	PriceHistory(date=date(2013, 11, 29),
		price=2500.00,
		volume=585000,
		total_btc=12054375,
		).save()
	PriceHistory(date=date(2012, 06, 28),
		price=25.98,
		volume=182500,
		total_btc=1054375,
		).save()

class Migration(migrations.Migration):

    dependencies = [
        ('historical_data', '0002_auto_20150421_0351'),
    ]

    operations = [
    migrations.RunPython(load_data)
    ]
