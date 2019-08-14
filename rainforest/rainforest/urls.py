"""rainforest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rainforest.views import *

urlpatterns = [
    path("", root),
    path('admin/', admin.site.urls),
    path('rainforest/products/', products_home ),
    path('rainforest/products/<int:id>', show_product, name='product_details'),
    path('rainforest/products/new', new, name='new_product'),
    path('rainforest/products/create', create, name='create_product'),
    path('rainforest/products/<int:id>/edit', edit_view, name='edit_view'),
    path('rainforest/products/<int:id>/editcreate', edit_create, name='edit_create'),
    path('rainforest/products/<int:product_id>/delete', delete_product, name='delete_product'),
    path('rainforest/products/<int:product_id>/new_review', new_review, name = 'new_review'),
    path('rainforest/products/<int:product_id>/create_review', create_review, name = 'create_review'),
    path('rainforest/products/<int:product_id>/review/<int:review_id>', show_review, name = 'show_review'),
    path('rainforest/products/<int:product_id>/review/<int:review_id>/edit', edit_review, name = 'edit_review'),
    path('rainforest/products/<int:product_id>/review/<int:review_id>/make_edit', make_review_edit, name = 'make_review_edit')
]
