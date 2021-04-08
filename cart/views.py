from django.shortcuts import render, redirect, get_object_or_404
from product.models import Game
from .forms import CheckForm
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist
"""
import stripe
from  django.conf import settings
"""


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request, game_id):
    game = Game.objects.get(id=game_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id=_cart_id(request)
        )
        cart.save()

    try:
        cart_item = CartItem.objects.get(game=game, cart=cart)
        if cart_item.quantity < cart_item.game.stock:
            cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            game=game,
            quantity=1,
            cart=cart
        )
        cart_item.save()
    return redirect('cart:cart_detail')


def remove_cart(request, game_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    game = get_object_or_404(Game, id=game_id)
    cart_item = CartItem.objects.get(game=game, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart:cart_detail')


def remove_full(request, game_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    game = get_object_or_404(Game, id=game_id)
    cart_item = CartItem.objects.get(game=game, cart=cart)
    cart_item.delete()
    return redirect('cart:cart_detail')


def check_out(request):
    context = {}
    form = CheckForm()
    context['form'] = form
    temp = request.POST.get('check')
    print(temp)
    if request.method == 'POST':
        form = CheckForm(request.POST)
        if form.is_valid():
            chi = form.cleaned_data['check']
            print(chi)
            form.save()

    return render(request, "cart/cart.html", context)


def cart_detail(request, ctotal=0, total=0, counter=0, cart_items=None, checkout=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        checkout = CartItem.objects.filter(cart=cart, check=True)
        cart_items = CartItem.objects.filter(cart=cart, active=True)

        for cart_item in checkout:
            ctotal += (cart_item.game.price * cart_item.quantity)
            counter += cart_item.quantity

        for cart_item in cart_items:
            total += (cart_item.game.price * cart_item.quantity)
            counter += cart_item.quantity

    except ObjectDoesNotExist:
        pass

    return render(request, 'cart/cart.html',
                  dict(checkout=checkout, ctotal=ctotal, cart_items=cart_items, total=total, counter=counter))
