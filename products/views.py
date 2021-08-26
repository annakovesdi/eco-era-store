from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Product, Category
from .forms import ProductForm, CategoryForm


def all_products(request):
    products = Product.objects.all()
    category = None

    if request.GET:
        if 'category' in request.GET:
            category = request.GET['category'].split(',')
            products = products.filter(category__name__in=category)
            category = Category.objects.filter(name__in=category)

    context = {
        'products': products,
        'category': category,
    }
    return render(request, "products/products.html", context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }
    return render(request, "products/product_detail.html", context)


@login_required
def product_management(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, "products/product_management.html", context)


@login_required
def add_category_description(request, id):
    if not request.user.is_superuser:
        messages.error('Only an Admin can access this page')
        return redirect(reverse('home'))
    category = get_object_or_404(Category, pk=id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Succesfully edited category description')
            return redirect(reverse('product_management'))
        else:
            messages.error(request, 'Failed to add category description.'
                                    'Please check your input.')
    else:
        form = CategoryForm(instance=category)
        messages.info(request, f'You are editing {category.name}')

    template = 'products/add_category_description.html'
    context = {
        'category': category,
        'form': form,
    }
    return render(request, template, context)

# add item to the store
@login_required
def add_item(request):
    if not request.user.is_superuser:
        messages.error('Only an Admin can access this page')
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Succesfully added item')
            return redirect(reverse('product_management'))
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
@login_required
def edit_item(request, product_id):
    if not request.user.is_superuser:
        messages.error('Only an Admin can access this page')
        return redirect(reverse('home'))
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully edited item')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to edit item. Please check your input.')
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
@login_required
def delete_item(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, 'Only an Admin can access this page')
        return redirect(reverse('home'))
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Succesfully deleted item')
    return redirect(reverse('product_management'))
