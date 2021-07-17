from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There is nothing in your bag at the moment")
        return redirect(reverse('products'))
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JEAGqLwodiuLrcyNeadLYXg'
                             'fvgpmGnZ9CemR1sQKd2Ru8cK5jWA6At1ZSz2REJz'
                             'VqxeGgpri8pYVu0WyQnZ0QBq00BEIeGctv',
        'client_secret': 'test client secret',
    }
    return render(request, template, context)
