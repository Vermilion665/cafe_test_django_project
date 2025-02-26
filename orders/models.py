from django.db import models
from django.urls import reverse


class Item(models.Model):
    dish_name = models.CharField(max_length=100, unique=True)
    price = models.FloatField()

    def __str__(self):
        return self.dish_name


class Order(models.Model):
    table_number = models.IntegerField()
    items = models.ManyToManyField(Item, related_name='items')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=10, choices=[
        ('waiting', 'В ожидании'),
        ('ready', 'Готово'),
        ('paid', 'Оплачено'),
    ], default='waiting')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['status', 'id']

    def __str__(self):
        return f'заказ #{self.id}'

    def get_absolute_url(self):
        return reverse('orders:order_detail', args=[str(self.id)])

    def save(self, *args, **kwargs):
        self.total_price = sum(item.price for item in self.items.all())
        super().save(*args, **kwargs)
