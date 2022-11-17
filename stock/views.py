# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from .models import Stock
# from .serializer import StockSerializer
# from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# from .handlers import calculate_expected_return, fair_value_calculator

# @api_view(['GET'])
# def get_stocks(request):
#     try:
#         stocks = Stock.objects.exclude(expectedReturn__exact=None)
        
#         page = request.GET.get('page')
#         results = 10
#         paginator = Paginator(stocks, results)
        
#         try:
#             stocks = paginator.page(page)
#         except PageNotAnInteger:
#             page = 1
#             stocks = paginator.page(page)
#         except EmptyPage:
#             page = paginator.num_pages()
#             stocks = paginator.page(page) 
        
#         serializer = StockSerializer(stocks, many=True)
#         return Response(serializer.data)
#     except Stock.DoesNotExist:
#         return Response({
#             'error': 'An error occurred while retrieving the stocks data'
#         })

# @api_view(['GET', 'DELETE'])
# def get_stock(request, symbol):
#     if request.method == 'GET':
#         try:
#             stock = Stock.objects.get(symbol=symbol)
#             serializer = StockSerializer(stock, many=False)
#             return Response(serializer.data)
#         except Stock.DoesNotExist:
#             return Response({
#                 'error': 'stock not found'
#             })
#     elif request.method == 'DELETE':
#         try:
#             stock = Stock.objects.get(symbol=symbol)
#             stock.delete()
#             return Response('Stock deleted successfully')
#         except Stock.DoesNotExist:
#             return Response({
#                 'error': 'stock not found'
#             })

# @api_view(['POST'])
# def add_stock(request):
#     serializer = StockSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({
#             'message': 'stock added successfully'
#         })
#     return Response({
#         'error': 'Cannot add stock'
#     })

# @api_view(['POST'])
# def calculate_fair_value(request):
#     stocks = Stock.objects.all()
#     for stock in stocks:
#         fair_value = fair_value_calculator(stock)
#         if fair_value != 0:
#             stock.fairValue = fair_value
#             stock.expectedReturn = round(calculate_expected_return(stock, fair_value), 0)
#             stock.save()
#             print(stock.symbol)
#     return Response({
#         'message': 'Fair value calculation successfully'
#     })
