from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product, Category
# Create your views here.


# View the shopping bag
def view_bag(request):
    return render(request, "shoppingbag/bag.html")


# Add an item to the shopping bag
def add_to_bag(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    bag = request.session.get('bag', {})
    get_quantity = request.POST.get('quantity')
    
    if get_quantity is None:
        quantity = 1
    else:
        quantity = int(get_quantity)

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(
            request, f'Updated {product.name} quantity to {bag[item_id]}')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your shoppingbag')
    
    request.session['bag'] = bag
    return redirect('products')


def add_wipes_to_bag(request, item_id):
    wipe = get_object_or_404(Product, pk=item_id)
    bag = request.session.get('bag', {})
    quantity = int(request.POST.get('quantity'))
    oil = get_object_or_404(Product, name="oil")
    print(oil)
    spray = get_object_or_404(Product, name="spray")
    print(spray)

    if oil or spray:
        print("There was oil or spray in post!")
        bag[item_id] = 1
        bag[oil.id] = 1
        bag[spray.id] = 1

    
    request.session['bag'] = bag

    return render(request, "shoppingbag/bag.html")



# Adjust items in shopping bag
def adjust_bag(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(
            request, f'Updated {product.name} quantity to {bag[item_id]}')
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your shoppingbag')

    print(bag)
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    try:
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        request.session['bag'] = bag
        messages.success(request, f'Removed {product.name} from your shoppingbag')
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
