from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category
from .forms import ProductForm


def product_views(request):
    products = Product.objects.order_by('-id')[:9]
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'pages/product.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, id=pk)
    context = {
        'product': product
    }
    return render(request, 'pages/pro_detail.html', context)

