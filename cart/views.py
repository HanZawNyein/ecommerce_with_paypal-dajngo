from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

# myshop
from myshop.models import Product

# cart
from cart.cart import Cart
from cart.forms import CartAddProductForm


# Create your views here.

@require_POST
def card_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], override_quantity=cd["override"])
    return redirect('cart:cart_detail')


@require_POST
def card_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product=product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'override': True})
    context = {
        'cart': cart
    }
    return render(request=request, template_name='cart/detail.html', context=context)
