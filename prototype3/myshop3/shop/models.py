from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list', args=[self.slug])


class Manufacturer(models.Model):
    name = models.CharField(max_length=45, help_text="Enter name of manufacturer")
    description = models.TextField(help_text="Enter description of manufacturer")
    email = models.EmailField(help_text="Enter email of user", blank=True)
    website = models.CharField(max_length=128, help_text="It is address of website", blank=True)

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

    # Methods
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('manufacturer-detail', args=[str(self.id)])


class Product(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    manufacturer_id = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    main_image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    detail_image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
