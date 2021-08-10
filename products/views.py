from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages

from .models import Product, Category
from .forms import ProductForm


def all_products(request):
    products = Product.objects.all()
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    context = {
        'products': products,
        'current_categories': categories,
    }
    return render(request, "products/products.html", context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }
    return render(request, "products/product_detail.html", context)


# add item to the store
def add_item(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Succesfully added item')
            return redirect(reverse('add_item'))
        else:
            messages.error(request, 'Failed to add item. Please check your input.')
    else: 
        form = ProductForm()
    form = ProductForm
    template = 'products/add_item.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


# edit an item
def edit_item(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully edited item')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to edit item. Please check your input.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_item.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


# delete item
def delete_item(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Succesfully deleted item')
    return redirect(reverse('products'))
