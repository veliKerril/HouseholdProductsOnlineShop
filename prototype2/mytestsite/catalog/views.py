from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm

# Опять же, спасибо django за готовую форму аутентификации.
from django.contrib.auth.forms import AuthenticationForm

# Функция для установки сессионного ключа.
# По нему django будет определять, выполнил ли вход пользователь.
from django.contrib.auth import login

from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout

# Create your views here.

from .models import User, Order, Good, Category, Manufacturer
from django.views import generic


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

    # Вычисляем, сколько раз человек побывал на домашней странице.
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_goods': num_goods, 'num_categories': num_categories,
                 'num_manufacturer': num_manufacturer, 'num_goods_available': num_goods_available,
                 'num_visits': num_visits},
    )


class GoodListView(generic.ListView):
    model = Good


class GoodDetailView(generic.DetailView):
    model = Good


class CategoryListView(generic.ListView):
    model = Category


class CategoryDetailView(generic.DetailView):
    model = Category


class ManufacturerListView(generic.ListView):
    model = Manufacturer


class ManufacturerDetailView(generic.DetailView):
    model = Manufacturer


class BasketListView(generic.ListView):
    model = Good


class FavoriteListView(generic.ListView):
    model = Good


def basket(request):

    return render(
        request,
        'basket.html',
    )


def favorites(request):

    return render(
        request,
        'favorites.html',
    )


def contacts(request):

    return render(
        request,
        'contacts.html',
    )


def authorization(request):
    return render(
        request,
        'authorization.html',
    )


def find(request):
    return render(
        request,
        'find.html',
    )


class SearchGoodList(generic.ListView):
    model = Good
    template_name = 'search_goods.html'

    def get_queryset(self):
        good_search = self.request.GET.get('search_good')
        return Good.objects.filter(name__icontains=good_search)


class RegisterFormView(FormView):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm

    # Аналогично регистрации, только используем шаблон аутентификации.
    template_name = "login.html"

    # В случае успеха перенаправим на главную.
    success_url = "/"

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        # Выполняем выход для пользователя, запросившего данное представление.
        logout(request)

        # После чего, перенаправляем пользователя на главную страницу.
        return HttpResponseRedirect("/")

