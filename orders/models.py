from django.db import models
from django.urls import reverse

STATUS_CHOICES = (
    ("in_waiting", "В ожидании"),
    ("ready", "Готово"),
    ("paid", "Оплачено"),
)

STATUS_MAP = dict(STATUS_CHOICES)
reverse_status_map = {v.lower(): k for k, v in STATUS_MAP.items()}


class Item(models.Model):
    dish_name = models.CharField(max_length=100, unique=True, verbose_name='Название блюда')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=1.00, verbose_name='Цена')

    def __str__(self):
        return self.dish_name


class Order(models.Model):
    table_number = models.PositiveSmallIntegerField(verbose_name='Номер столика', default=1)
    items = models.ManyToManyField(Item, blank=True, verbose_name='Блюда')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name='Сумма заказа')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='in_waiting', verbose_name='Статус')

    def calculate_total_price(self):
        return self.items.aggregate(total=models.Sum('price'))['total'] or 0.00
    
    def get_absolute_url(self):
        return reverse("orders:order-detail", kwargs={"pk": self.id})
    
    def __str__(self):
        return str({self.id})
    