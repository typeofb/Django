from django.shortcuts import render
import logging
from .models import Stock

logger = logging.getLogger(__name__)

# Create your views here.
def stock_list(request):
    logger.debug('request stock_list')

    stocks = Stock.objects.raw("SELECT id, category, name, price, cnt, img FROM stock")
    logger.debug(list(stocks))

    return render(request, 'stock/stock_list.html', {'stocks': stocks})