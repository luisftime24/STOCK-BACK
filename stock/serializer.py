from rest_framework import serializers
from .models import Stock


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = [
            'id', 'symbol', 'currentPrice',
            'fairValue', 'totalDebt', 'totalCash',
            'freeCashflow', 'netIncomeToCommon', 'pegRatio',
            'logo_url', 'shortName', 'expectedReturn', 'sharesOutstanding'
        ]

class OneStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'
