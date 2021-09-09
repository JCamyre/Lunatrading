from rest_framework import generics, status, viewsets
from .serializers import StockSerializer, PortfolioSerializer, CreatePortfolioSerializer
from .models import Portfolio, Stock
from .methods import add_stocks, delete_duplicate_stocks, test_stocks
from rest_framework.views import APIView
from rest_framework.response import Response
import py_trading
import os
from django.views import View
from django.http import HttpResponse, HttpResponseNotFound


# So the frontend.views handles the rendering of the index.html, which contains code for reactjs.
# Then api.views handles the backend/logic of the webpages. Specific views handles specific urls.


class Assets(View):

    def get(self, _request, filename):  # Handling when a HttpResponse is sent to user
        # The views.py in your React frontend needs a content_type argument in the HttpResponse.
        # Heroku needs to know where the static files are.

        # The "refused to execute script ... MIME type ('text/html')" problem stems from Django's default content_type setting for an HttpResponse, which is text/html.

        # This can be fixed by including a content_type='application/javascript' argument in the return statement of a new class-based view called Assets(View) inside views.py like so:
        path = os.path.join(os.path.dirname(__file__), 'static', filename)

        if os.path.isfile(path):
            with open(path, 'rb') as file:
                return HttpResponse(file.read(), content_type='application/javascript')
        else:
            return HttpResponseNotFound()


class PortfolioView(generics.ListAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer


class StocksView(viewsets.ModelViewSet):
    serializer_class = StockSerializer
    queryset = Stock.objects.all()


# class CreatePortfolioView(APIView):
#     serializer_class = CreatePortfolioSerializer

#     # Post request from the user when creating a new portfolio. View processing their information.
#     def post(self, request, format=None):

#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             stocks = serializer.data.get('stocks')

#             portfolio = Portfolio(stocks=stocks)
#             portfolio.save()
#             return Response(PortfolioSerializer(portfolio).data, status=status.HTTP_201_CREATED)

#         return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)


# class UpdatePortfolioView(APIView):
#     pass


# class GetStockInfo(APIView):
#     serializer_class = StockSerializer

#     def get(self, request, format=None):
#         ticker = request.GET['ticker'].upper()

#         if ticker != None:
#             stock = Stock.objects.filter(ticker=ticker)
#             if len(stock) > 0:
#                 stock = stock[0]
#                 data = StockSerializer(stock).data
#                 # Idk how to access data likes this
#                 data['ticker'] = stock.ticker
#                 # Have to have attribute for Stock models for the due_diligence information
#                 try:
#                     current_stock = Stock.objects.all().filter(
#                         ticker=stock.ticker)[0].ticker
#                     current_stock = py_trading.Stock(current_stock)
#                 except:
#                     print('ERROR')
#                     return Response({'Stock not found': 'Not supported exchange.'}, status=status.HTTP_404_NOT_FOUND)

#                 # If I have to generate all of this information everytime someone clicks on a stock, what's the point of having a database for these stocks? All I need is the GetAllStocks view for homepages and get the ticker string, and use py_trading.Stock(ticker)
#                 # IDK, SOMETIMES RANDOMLY DOESN'T WORK... SOMETHING IN THIS TRY STATEMENT IS FAILING.

#                 due_diligence_data = current_stock.financials()  # Should I convert to dictionary?
#                 # I'M PRETTY SURE THE LABEL AND VALUE IN THE DF CHANGE SOMETIMES, IDK WHY

#                 # Really janky fix for now, seemingly .financials() labels and values r random (sometimes swapped, sometimes not)

#                 data_dict = {key: val for key,
#                              val in due_diligence_data.values.tolist()}
#                 try:
#                     data['data2'] = data_dict['Insider Own'], data_dict[
#                         'Shs Float'], data_dict['RSI (14)']
#                 except:
#                     data_dict = {key: val for key, val in zip(
#                         due_diligence_data[0]['Value'], due_diligence_data[0]['Label'])}
#                     data['data2'] = data_dict['Insider Own'], data_dict[
#                         'Shs Float'], data_dict['RSI (14)']

#                 data_dict['Shs Float'] = data_dict['Shs Float'][:-1]
#                 data['data1'] = data_dict
#                 data['data3'] = data_dict['Volatility'], data_dict['Rel Volume'], data_dict['Volume']

#                 data['table_data'] = [['Price', data_dict['Price']], ['Short Float', data_dict['Short Float']],
#                                       ['Market Cap', data_dict['Market Cap']], [
#                                           'Forward P/E', data_dict['Forward P/E']],
#                                       ['Avg Volume', data_dict['Avg Volume']]]

#                 return Response(data, status=status.HTTP_200_OK)

#             return Response({'Stock not found': 'Invalid Ticker.'}, status=status.HTTP_404_NOT_FOUND)


# class StockTechnicals(APIView):
#     def get(self, request, format=None):
#         ticker = request.GET['queried_ticker']

#         if ticker != None:
#             stock_result = Stock.objects.filter(ticker=ticker)
#             if len(stock_result) > 0:
#                 stock = stock_result[0]

#                 try:
#                     stock = py_trading.Stock(stock.ticker)
#                 except:
#                     return Response({'Stock not supported by exchange': 'Not supported exchange.'}, status=status.HTTP_404_NOT_FOUND)

#                 data = {}
#                 data['technicals'] = stock.ta_indictators()
#                 data['activity'] = stock.big_money()
#                 data['short-selling'] = stock.short_selling()

#                 # adl calculation: ((Close - Low) - (High - Close))/(High - Low) * period's volume. We'll do it for one month.
#                 data['adl'] = stock.adl()
#                 print(data['adl'])

#                 return Response(data, status=status.HTTP_200_OK)

#         return Response({'Bad Request': 'This stock does not exist or is not part of our database, sorry!'})


# class StockNews(APIView):  # Inform users they have to wait because have to wait for api to load

#     def get(self, request, format=None):
#         ticker = request.GET['ticker']

#         if ticker != None:
#             stock_result = Stock.objects.filter(ticker=ticker)
#             if len(stock_result) > 0:
#                 stock = stock_result[0]

#                 try:
#                     stock = py_trading.Stock(stock.ticker)
#                 except:
#                     print('ERROR with ticker not loading, prob api related')
#                     return Response({'Stock not supported by exchange': 'Not supported exchange.'}, status=status.HTTP_404_NOT_FOUND)

#                 data = {}
#                 stock_news = stock.news_sentiments()[4]
#                 for article in stock_news:
#                     article['date'] = article['datetime'].strftime('%m %d %Y')
#                 stock_news = sorted(
#                     stock_news, key=lambda x: x['datetime'], reverse=True)

#                 sectors_news = stock.news_sentiments()[3]
#                 for sector in sectors_news:
#                     for article in sector:
#                         article['date'] = article['datetime'].strftime(
#                             '%m %d %Y')

#                 data['stock-news-sentiment'] = stock_news[:5]
#                 data['sectors-news-sentiment'] = [sector_news[:3]
#                                                   for sector_news in sectors_news]

#                 # data['social-media'] = stock.social_media_sentiment()
#                 return Response(data, status=status.HTTP_200_OK)

#         return Response({'Bad Request': 'This stock does not exist or is not part of our database, sorry!'})


# class FindStock(APIView):
#     lookup_url_kwarg = 'ticker'

#     def post(self, request, format=None):
#         if not self.request.session.exists(self.request.session.session_key):
#             self.request.session.create()

#         ticker = request.data.get(self.lookup_url_kwarg)

#         if ticker != None:
#             stock_result = Stock.objects.filter(ticker=ticker)
#             if len(stock_result) > 0:  # If the stock exists
#                 stock = stock_result[0]

#                 self.request.session['ticker'] = stock.ticker
#                 return Response({'message': 'You are viewing the stock!'}, status=status.HTTP_200_OK)

#             return Response({'Bad Request': 'This stock does not exist or is not part of our database, sorry!'}, status=status.HTTP_404_NOT_FOUND)

#         return Response({'Bad Request': 'Invalid post data, did not find a ticker'}, status=status.HTTP_400_BAD_REQUEST)


# class GetSearchedStock(APIView):

#     def get(self, request, format=None):
#         ticker = request.GET['queried_ticker']
#         queried_stocks = Stock.objects.filter(ticker__startswith=ticker)
#         queried_stocks = [{'ticker': StockSerializer(stock).data['ticker'], 'name': StockSerializer(
#             stock).data['name']} for stock in queried_stocks]
#         data = {}
#         data['queried_ticker'] = sorted(
#             queried_stocks, key=lambda x: x['ticker'])
#         print(data)

#         return Response(data, status=status.HTTP_200_OK)
