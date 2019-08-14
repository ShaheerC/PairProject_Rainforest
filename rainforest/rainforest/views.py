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
    reviews = Review.objects.filter(product = product)
    context = {'product': product, 'reviews': reviews}
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

def edit_view(request, id):
    product = Product.objects.get(pk=id)
    form = ProductForm(instance = product)
    context = {"form": form, 'product': product}
    return render(request, 'edit.html', context)

def edit_create(request, id):
    product = Product.objects.get(pk=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance = product)
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
   
def new_review(request, product_id):
    product = Product.objects.get(pk = product_id)
    form = ReviewForm()
    context = {'form': form, 'product': product, 'action': 'create_review'}
    response = render(request, 'new_review.html', context)
    return HttpResponse(response)

def create_review(request, product_id):
    product = Product.objects.get(pk = product_id)
    form = ReviewForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit = False)
        new_review.product = product
        new_review.save()
        return HttpResponseRedirect(f'/rainforest/products/{product_id}')
    else:
        context = {'form': form, 'product': product, 'action': 'create_review'}
        return render(request, 'new_review.html', context)

def show_review(request, product_id, review_id):
    review = Review.objects.get(id = review_id)
    context = {'review': review}
    response = render(request, 'show_review.html', context)
    return HttpResponse(response)

def edit_review(request, product_id, review_id):
    review = Review.objects.get(pk = review_id)
    product = Product.objects.get(pk = product_id)
    form = ReviewForm(instance = review)
    context = {'form': form, 'product': product, 'review': review}
    response = render(request, 'edit_review.html', context)
    return HttpResponse(response)

def make_review_edit(request, product_id, review_id):
    product = Product.objects.get(pk = product_id)
    review = Review.objects.get(pk = review_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance = review)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            content = form.cleaned_data.get('content')
            review.name = name
            review.content = content
            review.save()
            return HttpResponseRedirect(f'/rainforest/products/{product_id}')
    form = ReviewForm(request.POST)
    context = {'from': form, 'product': product, 'review':review}
    response = render(request, 'edit.html', context)
    return HttpResponse(response)
