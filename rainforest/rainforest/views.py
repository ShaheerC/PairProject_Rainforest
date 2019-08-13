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

def new(request):
    form = ProductForm()
    context = {"form": form, "message": "Create new product", "action": "/rainforest/products/create"}
    return render(request, 'form.html', context)

def create(request):
    form = ProductForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/rainforest/products")
    else:
        context = {'form': form}
        return render(request, 'form.html', context)

def delete_product(request, product_id):
    product = Product.objects.get(id = product_id)
    product.delete()
    return HttpResponseRedirect('/rainforest/products')

def edit(request, id):
    product = Product.objects.get(pk=id)
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            description = form.cleaned_data.get('description')
            price_in_cents = form.cleaned_data.get('price_in_cents')
            product.name = name
            product.description = description
            product.price_in_cents = price_in_cents
            product.save()
            return HttpResponseRedirect(f"/rainforest/products/{id}")
    form = ProductForm(request.POST)
    context = {'product': product, 'form': form}
    return HttpResponse(render(request, 'edit.html', context))
    

