from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']

        labels = {
            "first_name": "",
            "last_name": "",
            "email": "",
            "address": "",
            "postal_code": "",
            "city": "",
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Имя'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Фамилия'}),
            'email' : forms.TextInput(attrs={'placeholder': 'E-mail'}),
            'address' : forms.TextInput(attrs={'placeholder': 'Адрес'}),
            'postal_code' : forms.TextInput(attrs={'placeholder': 'Индекс'}),
            'city' : forms.TextInput(attrs={'placeholder': 'Город'})
        }

