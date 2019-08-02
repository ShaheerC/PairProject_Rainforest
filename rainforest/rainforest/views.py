from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from rainforest.models import *

def products_home(request):
    context ={'products': Product.objects.all()}
    response = render(request, 'products.html', context)
    return HttpResponse(response)