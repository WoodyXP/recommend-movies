import self as self
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .ebay_api.ebay_connecter import get_kw, get_items, res_print
from .forms import ProductForm
import logger
# Create your views here.

def home(request):
    ctx = {}
    search_string = request.POST.get('product_inp')
    keyword = get_kw(search_string)
    items = get_items(keyword)
    product_list = res_print(items)
    ctx["Products"] = {"Products" : product_list}
    ctx["Prices"] = product_list
    return render(request, 'shop/index.html', ctx)

def get_product(request):
    ctx = {}
    if request.method != 'POST':
        search_string = request.POST.get('product_inp')
        keyword = get_kw(search_string)
        items = get_items(keyword)
        product_list = res_print(items)
        ctx["Products"] = {"Products" : product_list}
        ctx["Prices"] = product_list 
    return render(request, ctx)