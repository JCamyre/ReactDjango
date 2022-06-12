from django.db import models


def retrieve_all_stocks():
    Stock.objects.all().delete()

    for i in ['AAPL', 'AMZN', 'NFLX']:
        ticker = Stock()
        ticker.save(force_insert=True)

# Create your models here.


class Stock(models.Model):
    INDUSTRIES = [
        ("LGOODS", "Luxury Goods"),
        ("APPS", "Software - Application"),
        ("BIOTECH", "Biotechnology")
    ]

    symbol = models.CharField(
        primary_key=True, max_length=4, default='AAPL', unique=True)
    cur_price = models.FloatField(null=False)
    industry = models.CharField(
        max_length=40, choices=INDUSTRIES, default="BIOTECH")
    daily_high = models.FloatField(null=False)
    daily_low = models.FloatField(null=False)
    overseas = models.BooleanField(default=False)

    # Calculate the buy/sell signals
    def get_signals(self, symbol):
        return symbol

    def __str__(self):
        return self.symbol
