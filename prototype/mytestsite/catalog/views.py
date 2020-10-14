from django.shortcuts import render

# Create your views here.

from .models import User, Order, Good, Category, Manufacturer


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_goods = Good.objects.all().count()
    num_categories = Category.objects.all().count()
    num_manufacturer = Manufacturer.objects.all().count()
    # Доступные книги (статус = 'a')
    num_goods_available = Good.objects.filter(availability=True).count()

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_goods': num_goods, 'num_categories': num_categories,
                 'num_manufacturer': num_manufacturer, 'num_goods_available': num_goods_available},
    )