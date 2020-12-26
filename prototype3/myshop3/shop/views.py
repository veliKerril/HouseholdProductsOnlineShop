from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from orders.models import Order, OrderItem
from cart.forms import CartAddProductForm


def main(request):
    category = None
    num_goods = Product.objects.all().count()
    num_categories = Category.objects.all().count()
    num_manufacturer = 0
    num_goods_available = Product.objects.filter(available=True).count()
    return render(request,
                  'shop/product/index.html',
                  {'num_goods': num_goods,
                   'num_categories': num_categories,
                   'num_manufacturer': num_manufacturer,
                   'num_goods_available': num_goods_available})


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request,
                  'shop/product/detail.html',
                  {'product': product})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form})


def show_orders(request):
    orders = Order.objects.all()
    orders_item = OrderItem.objects.all()
    name_of_orders = request.user.first_name
    time_created = Order.created
    if not Order.paid:
        paid = "заказ оплачен"
    else:
        paid = "заказ не оплачен"
    return render(request, 'shop/product/orders.html', {'orders': orders, 'orders_item': orders_item,
                                                        'name_of_orders': name_of_orders, 'time_created': time_created,
                                                        'paid': paid})
