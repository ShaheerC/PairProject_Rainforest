from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from rainforest.models import *

def root(request):
    return HttpResponseRedirect("/rainforest/products")

def products_home(request):
    context ={'products': Product.objects.all()}
    response = render(request, 'products.html', context)
    return HttpResponse(response)

def show_product(request, id):
    product = Product.objects.get(pk=id)
    context = {'product': product}
    return render(request, 'product.html', context)