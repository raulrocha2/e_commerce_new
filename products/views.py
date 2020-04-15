# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import ListView

from .models import Product

#Class Based View
class ProductListView(ListView):
    #traz todos os produtos do banco de dados sem filtrar nada
    queryset = Product.objects.all()

#function Based View
def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'qs': queryset
    }
    return render(request, "products/list.html", context)
