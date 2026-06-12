from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, CartItem


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, "Welcome to Nrityalay! Your account has been created.")
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    auth_logout(request)
    return redirect('home')


def home(request):
    products = Product.objects.all()
    category = request.GET.get('category')
    if category:
        products = products.filter(category=category)

    categories = Product.objects.values_list('category', flat=True).distinct()

    return render(request, 'home.html', {
        'products': products,
        'categories': categories,
        'selected_category': category,
    })


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    messages.success(request, f"{product.name} added to your cart!")
    return redirect(request.POST.get('next') or 'home')


@login_required
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user).select_related('product')
    total = sum(item.subtotal() for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total})


@login_required
def update_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    action = request.POST.get('action')
    if action == 'increase':
        item.quantity += 1
        item.save()
    elif action == 'decrease':
        item.quantity -= 1
        if item.quantity <= 0:
            item.delete()
        else:
            item.save()
    elif action == 'remove':
        item.delete()
    return redirect('cart')


@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    if not cart_items.exists():
        messages.info(request, "Your cart is empty.")
        return redirect('cart')
    cart_items.delete()
    messages.success(request, "Thank you! Your order has been placed successfully.")
    return redirect('home')
