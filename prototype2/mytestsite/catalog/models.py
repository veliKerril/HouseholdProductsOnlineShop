from django.db import models
from django.urls import reverse

# Create your models here.


class User(models.Model):
    # Fields
    # id = models.IntegerField(help_text="It is primary key", primary_key = True)
    name = models.CharField(max_length=45, help_text="Enter name of user")
    last_name = models.CharField(max_length=45, help_text="Enter last name of user")
    patronymic = models.CharField(max_length=45, help_text="Enter patronymic of user")
    age = models.IntegerField(help_text="Enter age of user")
    email = models.EmailField(help_text="Enter email of user")
    phone_number = models.IntegerField(help_text="Enter phone number of user")
    address = models.CharField(max_length=225, help_text="Enter addres of user")
    login = models.CharField(max_length=45, help_text="Enter login of user")
    password = models.CharField(max_length=45, help_text="Enter password of user")

    # Methods
    def __str__(self):
        return self.name


class Order(models.Model):
    # Fields
    user_id = models.ForeignKey('User', help_text="It is foreign key of user", on_delete=models.SET_NULL, null=True)
    good_id = models.ForeignKey('Good', help_text="It is foreign key of good", on_delete=models.SET_NULL, null=True)
    order_datatime = models.DateTimeField()
    delivery_datatime = models.DateTimeField()
    status = models.CharField(max_length=45, help_text="It is status of our order")

    # Methods
    def __str__(self):
        return self.user_id + self.good_id


class Good(models.Model):
    # Fields
    # id = models.IntegerField(help_text="It is primary key", primary_key=True)
    id_manufacturer = models.ForeignKey('Manufacturer', help_text="It is foreign key of manufacturer", on_delete=models.SET_NULL, null=True)
    id_category = models.ForeignKey('Category', help_text="It is foreign key of category",
                                    on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=45, help_text="Enter name of good")
    description = models.TextField(help_text="Enter description of good")
    availability = models.BooleanField(help_text="Is this kind of good exist?")
    price = models.IntegerField(help_text="Enter price of good")
    count = models.IntegerField(help_text="Enter count of good")
    # sale = models.IntegerField(help_text="Enter count of sale", blank=True)
    picture = models.CharField(max_length=255, help_text="It is address image of good", blank=True)

    # Methods
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('good-detail', args=[str(self.id)])


class Category(models.Model):
    # Fields
    # id = models.IntegerField(primary_key=True, help_text="It is primary key")
    name = models.CharField(max_length=45, help_text="Enter name of category")
    description = models.TextField(help_text="Enter description of category")
    # availability = models.BooleanField(help_text="Is this kind of category exist?")
    picture = models.CharField(max_length=255, help_text="It is address image of category", blank=True)

    # Methods
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category-detail', args=[str(self.id)])


class Manufacturer(models.Model):
    # Fields
    # id = models.IntegerField(help_text="It is primary key", primary_key = True)
    name = models.CharField(max_length=45, help_text="Enter name of manufacturer")
    description = models.TextField(help_text="Enter description of manufacturer")
    email = models.EmailField(help_text="Enter email of user", blank=True)
    logo = models.CharField(max_length=255, help_text="It is address image of manufacturer", blank=True)
    website = models.CharField(max_length=128, help_text="It is address of website", blank=True)

    # Methods
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('manufacturer-detail', args=[str(self.id)])
