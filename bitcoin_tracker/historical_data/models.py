from django.db import models

class PriceHistory(models.Model):
	'tracking the price history of the mighty bitcoin'
	date = models.DateTimeField(auto_now_add=True)
	price = models.DecimalField(max_digits=8, decimal_places=2)
	volume = models.PositiveIntegerField()
	total_btc = models.PositiveIntegerField()
	market_cap = models.PositiveIntegerField(null=True)



