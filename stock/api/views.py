from rest_framework.decorators import api_view
from rest_framework.response import Response

from stock.models import Stock
from stock.serializer import StockSerializer, OneStockSerializer

@api_view(['GET'])
def get_stocks(request):
    stocks = Stock.objects.exclude(fairValue__lte=0).exclude(expectedReturn__exact=None)
    serializer = StockSerializer(stocks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_stocks_by_symbol(request, symbol):
    stock = Stock.objects.get(symbol=symbol)
    serializer = OneStockSerializer(stock, many=False)
    return Response(serializer.data)