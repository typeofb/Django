from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)

# Create your views here.
def stock_list(request):
    logger.debug('request stock_list')
    return render(request, 'stock/stock_list.html', {})