from django.contrib import admin

# Register your models here.

from .models import User, Order, Good, Category, Manufacturer

admin.site.register(User)
admin.site.register(Order)
admin.site.register(Good)
admin.site.register(Category)
admin.site.register(Manufacturer)