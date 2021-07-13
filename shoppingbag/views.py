from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from products.models import Product
# Create your views here.


# View the shopping bag
def view_bag(request):
    return render(request, "shoppingbag/bag.html")


# Add an item to the shopping bag
def add_to_bag(request, item_id):
    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity
    messages.success(request, f'Added {product.name} to your shoppingbag')
    request.session['bag'] = bag
    return redirect(redirect_url)


# Adjust items in shopping bag
def adjust_bag(request, item_id):
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id)

    print(bag)
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    try:
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)
        