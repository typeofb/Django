from django.shortcuts import render

# Create your views here.
def stock_list(request):
    return render(request, 'stock/stock_list.html', {})