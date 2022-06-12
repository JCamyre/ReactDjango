from rest_framework import serializers
from .models import Stock


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ('symbol', 'cur_price', 'industry',
                  'daily_high', 'daily_low', 'overseas')
